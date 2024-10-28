from django import forms
from .models import Categoria, Juego, Resena, User
from django.contrib.auth.forms import UserCreationForm


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre de la categoría'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Ingrese la descripción'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'accept': 'image/*'
            })
        }


class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'descripcion', 'fecha_lanzamiento', 'desarrollador',
                  'precio', 'requisitos', 'imagen', 'categorias']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título del juego'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Ingrese la descripción del juego'
            }),
            'fecha_lanzamiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'desarrollador': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del desarrollador'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio'
            }),
            'requisitos': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Ingrese los requisitos del sistema'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'accept': 'image/*'
            }),
            'categorias': forms.SelectMultiple(attrs={
                'class': 'form-control',
            })
        }


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['puntuacion', 'comentario']
        widgets = {
            'puntuacion': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu reseña aquí'
            })
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su correo electrónico'
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control'}
            
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'foto', 'bio', 'fecha_nacimiento']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellidos'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'accept': 'image/*'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Cuéntanos sobre ti'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
