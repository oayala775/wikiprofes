from django.shortcuts import render
from django.views import generic
from .models import Publicacion

# Create your views here.
class PublicacionView(generic.ListView):
    template_name = 'publicacion/index.html'

    def get_queryset(self):
        return Publicacion.objects.order_by('-fecha')[:5]

class ProfesorView(generic.ListView):
    template_name = "publicacion/profesor.html"

    def get_queryset(self):
        return Publicacion.objects.filter(profesor_id=self.kwargs["profesor_id"])

class MateriaView(generic.ListView):
    template_name = "publicacion/materia.html"

    def get_queryset(self):
        return Publicacion.objects.filter(materia_id=self.kwargs["materia_id"])