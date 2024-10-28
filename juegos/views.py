from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Categoria, Juego, Resena
from .forms import CategoriaForm, JuegoForm, ResenaForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse
# Dashboard


def index(request):
    if request.user.is_authenticated:
        return redirect('juegos:dashboard')
    return redirect('juegos:login')


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


@login_required
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


@login_required
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


@login_required
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
    return render(request, 'juegos/juego/detalle.html', {'juego': juego, 'resenas': resenas})


@login_required
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


@login_required
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


@login_required
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
    resenas = Resena.objects.filter(usuario=request.user)
    return render(request, 'juegos/resena/lista.html', {'resenas': resenas})


@login_required
def resena_create(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
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
    if request.user != resena.usuario:
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
    if request.user != resena.usuario:
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
