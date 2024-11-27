from django.shortcuts import render
from django.views import generic
from .models import Publicacion
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
        publicaciones = self.get_queryset()
        for publicacion in publicaciones:
            sumatoria += (
                publicacion.dominio
                + publicacion.puntualidad
                + publicacion.asistencia
                + publicacion.dificultad
                + publicacion.seguimiento
            ) / 5
        context["promedio_general"] = "%.1f" % (sumatoria / len(publicaciones))
        return context

class MateriaView(generic.ListView):
    template_name = "publicacion/materia.html"

    def get_queryset(self):
        return Publicacion.objects.filter(materia_id=self.kwargs["materia_id"])

class MateriaView(generic.ListView):
    template_name = "publicacion/materia.html"

    def get_queryset(self):
        return Publicacion.objects.filter(materia_id=self.kwargs["materia_id"])
    
class BusquedaView(generic.ListView):
    model = Materia
    template_name = "publicacion/busqueda.html"
    context_object_name = "materia_list"

    def get_queryset(self):
        materia_nombre = self.request.GET.get("materia_nombre", "")
        if materia_nombre:
            return Materia.objects.filter(nombre__icontains=materia_nombre)
        return Materia.objects.none() 