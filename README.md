# 🔥 Monitoramento de Queimadas (Projeto Acadêmico)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-%237EBC6F.svg?style=for-the-badge&logo=openstreetmap&logoColor=white)

Este projeto foi desenvolvido como um trabalho bimestral universitário. O sistema fornece uma plataforma centralizada para o registro e visualização de focos de incêndio, integrando dados geoespaciais com controle de acesso rigoroso para garantir a confiabilidade das informações.

## 📋 Sobre o Projeto

O sistema permite que qualquer pessoa visualize em tempo real a localização e a intensidade das queimadas. No entanto, para manter a integridade dos dados, apenas profissionais devidamente identificados podem realizar novos registros.

### Principais Funcionalidades:
* **Painel de Ocorrências:** Listagem intuitiva com o nome do local, coordenadas e nível de intensidade.
* **Mapa Interativo (OpenStreetMap):** Ao selecionar uma ocorrência na lista, o mapa renderiza automaticamente o ponto exato do foco de incêndio.
* **Controle de Acesso:** Área restrita para bombeiros. Apenas usuários cadastrados e que possuam credencial **CLB** (Bombeiro) podem adicionar novas ocorrências.

---

## 🛠️ Tecnologias e Arquitetura

O projeto utiliza uma stack moderna para garantir performance e facilidade de manutenção:
* **Linguagem:** Python
* **Framework Web:** Django (MTV Architecture)
* **Frontend:** HTML5, CSS3 (Design responsivo)
* **Mapas:** API OpenStreetMap
* **Banco de Dados:** SQLite (padrão de desenvolvimento)

### Colaboração do Grupo:
Este projeto foi o resultado de um esforço conjunto, com a seguinte divisão de responsabilidades:
* **Backend & Integração de APIs:** eu (Talyson) e Ícaro
* **Modelagem de Dados & Banco de Dados:** Júlia e Saulo
* **Interface (Templates & UI/UX):** Ronan

### Imagens
<img width="1919" height="926" alt="Screenshot_2" src="https://github.com/user-attachments/assets/8205d4af-a856-40f1-9ad5-f4b4fec3c286" />
</br></br>
<img width="1919" height="922" alt="Screenshot_3" src="https://github.com/user-attachments/assets/e12fe000-371e-4eb6-8d35-4fa2ad65916f" />
</br></br>
<img width="1919" height="917" alt="Screenshot_6" src="https://github.com/user-attachments/assets/939fc3aa-fd28-4d23-9c02-87d0ba64eba2" />
</br></br>
<img width="1919" height="925" alt="Screenshot_7" src="https://github.com/user-attachments/assets/ac0a913c-a60d-40c9-ad03-effe50788d5d" />
</br></br>
<img width="1919" height="923" alt="Screenshot_5" src="https://github.com/user-attachments/assets/2529668c-d6e4-4873-92dd-86e3f172ff1a" />


---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o ambiente em sua máquina local:

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/projeto-queimadas-naldo.git
cd projeto-queimadas-naldo
```

### 2. Configurar o Ambiente Virtual (VENV)
```bash
# Criar o ambiente
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Preparar o Banco e Carregar Dados Iniciais (Fixtures)
Como o projeto já possui usuários e configurações pré-definidas, basta rodar:
```bash
# Criar a estrutura das tabelas
python manage.py migrate

# Carregar os usuários e dados iniciais (Admin/Bombeiros)
python manage.py loaddata fixtures/*.json
```

### 5. Iniciar o Servidor
```bash
python manage.py runserver
```
Acesse no navegador: `http://127.0.0.1:8000/`

---

## 🔐 Credenciais de Acesso
O projeto já vem configurado com usuários de teste via fixtures para facilitar a avaliação.
> **Admin / Bombeiro:** Consulte o arquivo `acesso.txt` para verificar os logins e senhas pré-definidos que foram carregados no banco.

---
*Este é um projeto acadêmico sem fins lucrativos, desenvolvido para fins de aprendizado.*
