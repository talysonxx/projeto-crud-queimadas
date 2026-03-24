from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal, InvalidOperation
from .models import Usuario, Incendio

# chama o template responsável por mostrar a página principal (mapa, alertas, etc...).
def index(request):
    user_id = request.session.get('user_id')
    incendios = Incendio.objects.all()
    
    # verifica se o usuário fez login, caso tenha feito, verifica se o usuário logado é o administrador para mostrar campos que somente ele pode ver.
    if user_id:
        administrador = False
        
        # verifica se o usuário existe no banco. caso tenha ocorrido algum erro na busca pelo usuário ou verificação de seus dados, apenas retorna a página e os alertas de incêndio.
        try:
            usuario = Usuario.objects.get(id=user_id)
            if usuario.email == 'admin@gmail.com':
                administrador = True
            return render(request, 'crud_app/index.html', {'usuario': usuario, 'administrador': administrador, 'incendios': incendios})
        except ObjectDoesNotExist:
            return render(request, 'crud_app/index.html', {'incendios': incendios})   
    return render(request, 'crud_app/index.html', {'incendios': incendios})

# view responsável pelo cadastro de usuários. somente usuários não logados podem entrar.
def create(request):
    user_id = request.session.get('user_id')
    if user_id:
        return redirect('index')
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        clcb = request.POST.get('clcb')
        
        # verifica se email já tem cadastro.
        if Usuario.objects.filter(email=email).exists():
            # retorna a página, mas com um aviso.
            return render(request, 'crud_app/create.html', {'erro': 'Email já cadastrado.'})
        
        # tenta converter o clcb para um número inteiro. em caso de erro, retorna a página com um aviso.
        try:
            clcb = int(clcb)
        except ValueError:
            return render(request, 'crud_app/create.html', {'erro': 'digite um clcb válido. apenas números inteiros são aceitos.'})
        
        # criptografa a senha antes de mandar cadastrar no banco.
        hash_senha = make_password(senha)
        usuario_novo = Usuario.objects.create(nome=nome, email=email, senha=hash_senha, clcb=clcb)
        request.session['user_id'] = usuario_novo.id # define a sessão com o id do novo usuário cadastrado
        return redirect('index')
    
    return render(request, 'crud_app/create.html')

# view responsável pelo login do usuário.
def login(request):
    # caso o usuário já esteja logado, redireciona para a página principal
    if request.session.get('user_id'):
        return redirect('index')
    
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        # verifica se o email do usuário existe.
        if Usuario.objects.filter(email=email).exists():
            # pega os dados do usuário com o mesmo email digitado no banco de dados.
            usuario = Usuario.objects.get(email=email)
            # compara o hash da senha no banco com a senha digitada
            if check_password(senha, usuario.senha):
                # senha correta. define a sessão e redireciona para a página principal.
                request.session['user_id'] = usuario.id
                return redirect('index')
            else:
                # senha incoreta. retorna a página com um aviso.
                return render(request, 'crud_app/login.html', {'erro': 'Senha ou email incorretos.'})
        else:
            # caso o email não exista, retorna a página com um aviso.
            return render(request, 'crud_app/login.html', {'erro': 'Senha ou email incorretos.'})
        
    return render(request, 'crud_app/login.html')

# view responsável por destruir a sessão criada ao logar ou se cadastrar no sistema. acesso somente a usuários com sessão ativa.
def logout(request):
    # caso o usuário esteja logado, deleta a sessão
    if request.session.get('user_id'):
        del request.session['user_id']
        return redirect('index')
    
    return redirect('index')

# view responsável por atulizar as informações de cadastro do usuário.
def update(request):
    user_id = request.session.get('user_id')
    
    # caso não esteja logado, redireciona para a tela de login.
    if not user_id:
        return redirect('login')
    
    # no caso de algum erro do usuário não existir no banco, mostra a tela de página não encontrada padrão do django.
    usuario = get_object_or_404(Usuario, id=user_id)

    # enviou os dados no formulário
    if request.method == "POST":
        # verifica se existe algum usuário exceto o usuário que está tentando atualizar o cadastro possui o email digitado.
        if Usuario.objects.filter(email=request.POST.get('email')).exclude(id=usuario.id).exists():
            return render(request, 'crud_app/update.html', {'erro': 'Já existe um usuário com esse email.', 'usuario': usuario})
        # caso o usuário digite a mesma senha
        # if check_password(request.POST.get('senha'), usuario.senha):
        #     return render(request, 'crud_app/update.html', {'erro': 'Você digitou a mesma senha'})
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.clcb = int(request.POST.get('clcb'))
        
        # ele não precisa digitar uma senha nova. só atualiza caso ela tenha sido digitada.
        senha = request.POST.get('senha')
        if senha:
            usuario.senha = make_password(senha)
        usuario.save()

        return redirect('index')
    else:
        # método get. normalmente ao acessar a url.
        return render(request, 'crud_app/update.html', {'usuario': usuario})

# view responsável por criar os alertas de incêndio. somente usuários logados tem acesso.
def create_index(request):
    user_id = request.session.get('user_id')
    if user_id:
        usuario = Usuario.objects.get(id=user_id)
        if request.method == 'POST':
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            gravidade = request.POST.get('gravidade')
            local = request.POST.get('local')
            if gravidade not in ['grave', 'medio', 'baixo']:
                return redirect('index')
            
            # caso o usuário tenha enviado algum dado não esperado pelo banco de dados, não adiciona o alerta ao banco.
            try:
                nova_latitude = Decimal(latitude.replace(',', '.'))
                nova_longitude = Decimal(longitude.replace(',', '.'))
                Incendio.objects.create(usuario=usuario, latitude=nova_latitude, longitude=nova_longitude, local=local, gravidade=gravidade)
            except (InvalidOperation, TypeError):
                return redirect('index')
            return redirect('index')
    return redirect('index')

# view responsável por mostrar os alertas de incêndio adicinados pelo usuário. somente usuários logados têm acesso.
def user_info(request):
    user_id = request.session.get('user_id')
    if user_id:
        usuario = Usuario.objects.get(id=user_id)
        usuarios = ''
        # caso o usuário logado seja o administrador, mostra todos os alertas de incêndio registrados e os todos os usuários cadastrados. se for usuário comum, mostra apenas os alertas adicionados pelo mesmo.
        if usuario.email == 'admin@gmail.com':
            incendios = Incendio.objects.all()
            usuarios = Usuario.objects.exclude(id=user_id)
        else:
            incendios = Incendio.objects.filter(usuario=user_id)
        context = {'incendios': incendios, 'usuario': usuario, 'usuarios': usuarios}
        return render(request, 'crud_app/user_info.html', context)
    return redirect('login')

# view responsável por apagar o alerta de incêndio do banco. acesso somente aos usuários logados. usuários comuns podem apenas deletar os alertas adicionados por eles próprios. o administrador pode deletar qualquer alerta.
def delet_fire(request, incendio_id):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('index')

    # 1. Obtém o Usuario logado (para verificar se é Admin)
    try:
        current_user = Usuario.objects.get(id=user_id)
        is_admin = (current_user.email == 'admin@gmail.com')
    except Usuario.DoesNotExist:
        # Se o ID da sessão não for válido, redireciona
        return redirect('index')

    # 2. Obtém o Incendio a ser deletado
    try:
        incendio = Incendio.objects.get(id=incendio_id)
    except Incendio.DoesNotExist:
        return redirect('user_info')

    # 3. Verifica Autorização (Proprietário OU Administrador)
    is_owner = (incendio.usuario and incendio.usuario.id == user_id)

    # Bloqueia se NÃO for o proprietário E NÃO for o administrador
    if not is_owner and not is_admin:
        return redirect('user_info')

    if request.method == 'POST':
        deletar = request.POST.get('deletar')
        
        # usuário tem que ter digitado "sim" para confirmar a exclusão
        if deletar and deletar.strip().lower().replace(' ', '') == 'sim':
            incendio.delete()
            return redirect('user_info')
        else:
            # mensagem de erro se a confirmação falhar
            return render(request, 'crud_app/delet_fire.html', {'incendio': incendio, 'message': 'você deve digitar "sim" para confirmar a exclusão.'})
    
    return render(request, 'crud_app/delet_fire.html', {'incendio': incendio})

# view responsável por deletar um usuário do  banco. acessível apenas para o administrador. 
def delet_user(request, user_id):
    current_user = request.session.get('user_id')
    if not current_user:
        return redirect('index')
    try:
        logged_user = Usuario.objects.get(id=current_user)
        is_admin = (logged_user.email == 'admin@gmail.com')
    except Usuario.DoesNotExist:
        return redirect('index')
    if not is_admin:
        return redirect('user_info')
    try:
        user_to_delet = Usuario.objects.get(id=user_id)
    except Usuario.DoesNotExist:
        return redirect('user_info')
    
    # aqui é para assegurar que o usuário a ser excluído não é o administrador
    if user_to_delet.id == current_user:
        return redirect('user_info')
    
    # enviou os dados do formulário
    if request.method == 'POST':
        deletar = request.POST.get('deletar')

        # caso o administrador não tenha digitado a palavra ou ainda tenha digitado da forma correta, retorna a página com um aviso.
        if deletar and deletar.strip().lower().replace(' ', '') == 'sim':
            user_to_delet.delete()
            return redirect('user_info')
        else:
            return render(request, 'crud_app/delet_user.html',  {'user_to_delet': user_to_delet,'message': 'você deve digitar "sim" para confirmar a exclusão.'})
    return render(request, 'crud_app/delet_user.html', {'user_to_delet': user_to_delet})
