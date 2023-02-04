from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    body = models.TextField()
    imagen = models.CharField(max_length=300)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
