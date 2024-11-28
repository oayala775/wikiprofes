from django.shortcuts import render
from django.views import generic
from .models import Publicacion

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from .forms import PublicacionForm
from django.contrib.auth.models import User
from .models import Profesor
from .models import Materia
from django.db.models import Avg

# Create your views here.
class PublicacionView(generic.ListView):
    template_name = "publicacion/index.html"

    def get_queryset(self):
        return Publicacion.objects.order_by("-fecha")[:5]


class ProfesorView(generic.ListView):
    template_name = "publicacion/profesor.html"

    def get_queryset(self):
        return Publicacion.objects.filter(profesor_id=self.kwargs["profesor_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publicaciones = self.get_queryset()

        if publicaciones.exists():
            context["promedio_dominio"] = "%.1f" % (
                Publicacion.objects.filter(
                    profesor_id=self.kwargs["profesor_id"]
                ).aggregate(Avg("dominio", default=0))["dominio__avg"]
            )

            context["promedio_puntualidad"] = "%.1f" % (
                Publicacion.objects.filter(
                    profesor_id=self.kwargs["profesor_id"]
                ).aggregate(Avg("puntualidad", default=0))["puntualidad__avg"]
            )

            context["promedio_asistencia"] = "%.1f" % (
                Publicacion.objects.filter(
                    profesor_id=self.kwargs["profesor_id"]
                ).aggregate(Avg("asistencia", default=0))["asistencia__avg"]
            )

            context["promedio_dificultad"] = "%.1f" % (
                Publicacion.objects.filter(
                    profesor_id=self.kwargs["profesor_id"]
                ).aggregate(Avg("dificultad", default=0))["dificultad__avg"]
            )

            context["promedio_seguimiento"] = "%.1f" % (
                Publicacion.objects.filter(
                    profesor_id=self.kwargs["profesor_id"]
                ).aggregate(Avg("seguimiento", default=0))["seguimiento__avg"]
            )

            sumatoria = 0
            for publicacion in publicaciones:
                sumatoria += (
                    publicacion.dominio
                    + publicacion.puntualidad
                    + publicacion.asistencia
                    + publicacion.dificultad
                    + publicacion.seguimiento
                ) / 5
            context["promedio_general"] = "%.1f" % (sumatoria / len(publicaciones))
        else:
            context["promedio_dominio"] = 0.0
            context["promedio_puntualidad"] = 0.0
            context["promedio_asistencia"] = 0.0
            context["promedio_dificultad"] = 0.0
            context["promedio_seguimiento"] = 0.0
            context["promedio_general"] = 0.0
        return context

class MateriaView(generic.ListView):
    model = Materia
    template_name = "publicacion/materia.html"
    context_object_name = "materia_list"

    def get_queryset(self):
        return Materia.objects.filter(id=self.kwargs["materia_id"]) 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['publicacion_list'] = Publicacion.objects.filter(materia_id=self.kwargs["materia_id"]) 
        return context

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
            publicacion = form.save(commit=False)  # No guardes inmediatamente
            publicacion.usuario = request.user  # Asigna el usuario actual
            publicacion.save()  # Ahora guarda
            return redirect('publicacion:index')
        # En caso de error, vuelve a renderizar el formulario
        usuarios = User.objects.all()
        profesores = Profesor.objects.all()
        materias = Materia.objects.all()
        usuario_actual = request.user
        return render(request, 'publicacion/publicacion_form.html', {
            'form': form,
            'usuarios': usuarios,
            'profesores': profesores,
            'materias': materias,
            'usuario_actual': usuario_actual,
        })

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
            publicacion = form.save(commit=False)  # No guardes inmediatamente
            publicacion.usuario = request.user  # Asigna el usuario actual
            publicacion.save()  # Ahora guarda
            return redirect('publicacion:index')
        # En caso de error, vuelve a renderizar el formulario
        usuarios = User.objects.all()
        profesores = Profesor.objects.all()
        materias = Materia.objects.all()
        usuario_actual = request.user
        return render(request, 'publicacion/publicacion_form.html', {
            'form': form,
            'usuarios': usuarios,
            'profesores': profesores,
            'materias': materias,
            'usuario_actual': usuario_actual,
        })

    def get_queryset(self):
        return Publicacion.objects.filter(materia_id=self.kwargs["materia_id"])
    
class BusquedaMateriaView(generic.ListView):
    model = Materia
    template_name = "publicacion/busqueda_materia.html"
    context_object_name = "materia_list"

    def get_queryset(self):
        materia_nombre = self.request.GET.get("materia_nombre", "")
        if materia_nombre:
            return Materia.objects.filter(nombre__icontains=materia_nombre)
        return Materia.objects.none() 
    
class BusquedaProfesorView(generic.ListView):
    model = Profesor
    template_name = "publicacion/busqueda_profesor.html"
    context_object_name = "profesor_list"

    def get_queryset(self):
        profesor_nombre = self.request.GET.get("profesor_nombre", "")
        if profesor_nombre:
            return Profesor.objects.filter(nombre__icontains=profesor_nombre)
        return Profesor.objects.none() 