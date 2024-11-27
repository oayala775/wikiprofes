from django.urls import path
from . import views

app_name = "materia"
urlpatterns = [
    path("materias", views.MateriaView.as_view(), name="materias"),
]