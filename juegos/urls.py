from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from juegos.views import CustomLoginView

app_name = 'juegos'

urlpatterns = [
    # Dashboard
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='juegos:login'), name='logout'),
    path('register/', views.register, name='register'),
    # Agregar estas URLs al urlpatterns existente
    path('perfil/editar/', views.user_update, name='user_update'),
    path('perfil/<str:username>/', views.user_detail, name='user_detail'),

    # URLs para Categorías
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('categorias/crear/', views.categoria_create, name='categoria_create'),
    path('categorias/editar/<int:pk>/',
         views.categoria_update, name='categoria_update'),
    path('categorias/eliminar/<int:pk>/',
         views.categoria_delete, name='categoria_delete'),

    # URLs de Juegos
    path('juegos/', views.juego_list, name='juego_list'),
    path('juegos/<int:pk>/', views.juego_detail,
         name='juego_detail'),  # Añade esta línea
    path('juegos/crear/', views.juego_create, name='juego_create'),
    path('juegos/<int:pk>/editar/', views.juego_update, name='juego_update'),
    path('juegos/<int:pk>/eliminar/', views.juego_delete, name='juego_delete'),

    path('juegos/<int:juego_id>/resenas/crear/',
         views.resena_create, name='resena_create'),
    path('resenas/<int:pk>/editar/', views.resena_update, name='resena_update'),
    path('resenas/<int:pk>/eliminar/', views.resena_delete, name='resena_delete'),
    path('resenas/', views.resena_list, name='resena_list'),
    path('chat/', views.chat_view, name='chat'),
    path('chat/message/', views.chat_message, name='chat_message'),
]
