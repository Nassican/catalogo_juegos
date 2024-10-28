from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from juegos.views import CustomLoginView, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juegos.urls')),  # Incluimos las URLs de la app juegos
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
