from django.urls import path
from . import views

app_name = 'juegos'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # URLs para Categorías
    path('categorias/', views.categoria_list, name='categoria_list'),
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
]
