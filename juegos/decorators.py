from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_admin_role():
            return view_func(request, *args, **kwargs)
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('juegos:dashboard')
    return wrapper