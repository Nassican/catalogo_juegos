from django.db import models
from django.contrib.auth.models import User
import os


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        # Eliminar la imagen si existe
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super().delete(*args, **kwargs)


class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    desarrollador = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    requisitos = models.TextField()
    imagen = models.ImageField(upload_to='juegos/')
    categorias = models.ManyToManyField(Categoria)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        # Eliminar la imagen si existe
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super().delete(*args, **kwargs)


class Resena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return f"Reseña de {self.usuario.username} para {self.juego.titulo}"
