from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'), # cadastrar usuário.
    path('update/', views.update, name='update'), # atualizar informações do usuário.
    path('user_info/', views.user_info, name='user_info'), # mostra incêndios adicionados pelo usuário (mais informações caso for administrador).
    path('user_info/delet_fire/<incendio_id>', views.delet_fire, name='delet_fire'), # pega o id do do incêndio e chama a view que apaga o registro no banco de dados.
    path('user_info/delet_user/<user_id>', views.delet_user, name='delet_user'), # pega o id do usuário e chama a view que apaga o registro do usuário no banco de dados (apenas administrador).
    path('create_index', views.create_index, name='create_index'), # chama a view responsável por cadastrar o alerta de incêndio banco de dados.
]
