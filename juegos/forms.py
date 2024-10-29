from django import forms
from .models import Categoria, Juego, Resena, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



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


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Nombre de usuario',
            'autofocus': True,
            'autocomplete': 'username'
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        })
    )

    error_messages = {
        'invalid_login': 'Por favor, introduce un nombre de usuario y contraseña correctos.',
        'inactive': 'Esta cuenta está inactiva.'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg mb-3'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-lg mb-3'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg mb-3',
            'placeholder': 'Correo electrónico',
            'autocomplete': 'email'
        })
    )
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg mb-3',
            'placeholder': 'Nombre de usuario',
            'autocomplete': 'username'
        })
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg mb-3',
            'placeholder': 'Contraseña',
            'autocomplete': 'new-password'
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg mb-3',
            'placeholder': 'Confirmar contraseña',
            'autocomplete': 'new-password'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'Este campo es obligatorio'}
            if field.help_text:
                field.help_text = f'<small class="text-muted">{field.help_text}</small>'




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
