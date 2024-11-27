from django.shortcuts import render
from django.views import generic
from .models import Profesor


# Create your views here.
class ProfesoresView(generic.ListView):
    template_name = "profesores/profesores.html"

    def get_queryset(self):
        return Profesor.objects.all()
