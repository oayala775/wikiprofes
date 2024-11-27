from django.shortcuts import render
from django.views import generic
from .models import Publicacion

from typing import Any
from django.db.models.query import QuerySet
from .models import Publicacion
from django.shortcuts import render, redirect
from django.views import View
from .forms import PublicacionForm
from django.contrib.auth.models import User
from .models import Publicacion
from .models import Profesor
from .models import Materia

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
    

class PublicacionCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PublicacionForm()
        usuarios = User.objects.all()
        profesores = Profesor.objects.all()
        materias = Materia.objects.all()
        usuario_actual = request.user  # Usuario autenticado
        return render(request, 'publicacion/publicacion_form.html', {
            'form': form,
            'usuarios': usuarios,
            'profesores': profesores,
            'materias': materias,
            'usuario_actual': usuario_actual,
        })

    def post(self, request, *args, **kwargs):
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publicacion:index')
        usuarios = User.objects.all()
        profesores = Profesor.objects.all()
        materias = Materia.objects.all()
        usuario_actual = request.user  # Usuario autenticado
        return render(request, 'publicacion/publicacion_form.html', {
            'form': form,
            'usuarios': usuarios,
            'profesores': profesores,
            'materias': materias,
            'usuario_actual': usuario_actual,
        })
