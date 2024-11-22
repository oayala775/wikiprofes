from django.db import models

class Profesor(models.Model): 
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nombre}"