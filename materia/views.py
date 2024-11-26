from django.shortcuts import render
from django.views import generic
from .models import Materia

# Create your views here.
class MateriaView(generic.ListView):
    template_name = "materias/materias.html"

    def get_queryset(self):
        return Materia.objects.all()