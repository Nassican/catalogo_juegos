from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Categoria, Juego, Resena, User
from .forms import CategoriaForm, JuegoForm, ResenaForm, CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse
from .decorators import admin_required
# Dashboard


def index(request):
    if request.user.is_authenticated:
        return redirect('juegos:dashboard')
    return redirect('juegos:login')

@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    resenas = Resena.objects.filter(usuario=user)
    context = {
        'profile_user': user,
        'resenas': resenas
    }
    return render(request, 'juegos/user/detail.html', context)

@login_required
def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('juegos:user_detail', username=request.user.username)
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'juegos/user/form.html', {'form': form})


@login_required
def dashboard(request):
    total_juegos = Juego.objects.count()
    total_categorias = Categoria.objects.count()
    total_resenas = Resena.objects.count()
    context = {
        'total_juegos': total_juegos,
        'total_categorias': total_categorias,
        'total_resenas': total_resenas,
    }
    return render(request, 'juegos/dashboard.html', context)

# Vistas para Categoría


def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'juegos/categoria/lista.html', {'categorias': categorias})


@admin_required
def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('juegos:categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'juegos/categoria/form.html', {'form': form, 'action': 'Crear'})


@admin_required
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('juegos:categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'juegos/categoria/form.html', {'form': form, 'action': 'Editar'})


@admin_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()  # Esto llamará al método delete personalizado
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('juegos:categoria_list')
    return render(request, 'juegos/categoria/confirmar_eliminar.html', {'categoria': categoria})
# Vistas para Juego


def juego_list(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos/juego/lista.html', {'juegos': juegos})


def juego_detail(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    resenas = Resena.objects.filter(juego=juego)
    user_has_reviewed = False
    
    if request.user.is_authenticated:
        user_has_reviewed = Resena.objects.filter(juego=juego, usuario=request.user).exists()
    
    context = {
        'juego': juego,
        'resenas': resenas,
        'user_has_reviewed': user_has_reviewed
    }
    return render(request, 'juegos/juego/detalle.html', context)


@admin_required
def juego_create(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego creado exitosamente.')
            return redirect('juegos:juego_list')
    else:
        form = JuegoForm()
    return render(request, 'juegos/juego/form.html', {'form': form, 'action': 'Crear'})


@admin_required
def juego_update(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego actualizado exitosamente.')
            return redirect('juegos:juego_list')
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'juegos/juego/form.html', {'form': form, 'action': 'Editar'})


@admin_required
def juego_delete(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        juego.delete()  # Esto llamará al método delete personalizado
        messages.success(request, 'Juego eliminado exitosamente.')
        return redirect('juegos:juego_list')
    return render(request, 'juegos/juego/confirmar_eliminar.html', {'juego': juego})

# Vistas para Reseña


@login_required
def resena_list(request):
    if request.user.is_admin_role():
        resenas = Resena.objects.all()
    else:
        resenas = Resena.objects.filter(usuario=request.user)
    return render(request, 'juegos/resena/lista.html', {'resenas': resenas})


@login_required
def resena_create(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    
    # Verificar si el usuario ya tiene una reseña para este juego
    existing_review = Resena.objects.filter(usuario=request.user, juego=juego).exists()
    if existing_review:
        messages.error(request, 'Ya has publicado una reseña para este juego.')
        return redirect('juegos:juego_detail', pk=juego_id)
        
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.usuario = request.user
            resena.juego = juego
            resena.save()
            messages.success(request, 'Reseña creada exitosamente.')
            return redirect('juegos:juego_detail', pk=juego_id)
    else:
        form = ResenaForm()
    return render(request, 'juegos/resena/form.html', {'form': form, 'juego': juego})


@login_required
def resena_update(request, pk):
    resena = get_object_or_404(Resena, pk=pk)
    # Permitir edición si es el dueño de la reseña o es admin
    if request.user != resena.usuario and not request.user.is_admin_role():
        messages.error(request, 'No tienes permiso para editar esta reseña.')
        return redirect('juegos:juego_detail', pk=resena.juego.pk)

    if request.method == 'POST':
        form = ResenaForm(request.POST, instance=resena)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reseña actualizada exitosamente.')
            return redirect('juegos:juego_detail', pk=resena.juego.pk)
    else:
        form = ResenaForm(instance=resena)
    return render(request, 'juegos/resena/form.html', {'form': form, 'action': 'Editar', 'juego': resena.juego})


@login_required
def resena_delete(request, pk):
    resena = get_object_or_404(Resena, pk=pk)
    # Permitir eliminación si es el dueño de la reseña o es admin
    if request.user != resena.usuario and not request.user.is_admin_role():
        messages.error(request, 'No tienes permiso para eliminar esta reseña.')
        return redirect('juegos:juego_detail', pk=resena.juego.pk)

    if request.method == 'POST':
        juego_pk = resena.juego.pk
        resena.delete()
        messages.success(request, 'Reseña eliminada exitosamente.')
        return redirect('juegos:juego_detail', pk=juego_pk)
    return render(request, 'juegos/resena/confirmar_eliminar.html', {'resena': resena})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('juegos:dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'juegos/registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'juegos/registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, 'Inicio de sesión exitoso.')
        return reverse('juegos:dashboard')

