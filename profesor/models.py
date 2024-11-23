from django.db import models
from django.contrib.auth.models import User


class Profesor(models.Model): 
    nombre = models.CharField(max_length=80)
    usuarios = models.ManyToManyField(User, through='publicacion.Publicacion')

    def __str__(self):
        return f"{self.nombre}"