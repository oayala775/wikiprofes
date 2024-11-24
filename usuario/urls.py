from django.urls import path
from . import views

#Establecer vistas y url correspondiente
app_name = 'usuario'
urlpatterns = [
    path('registro', views.RegistriView.as_view(), name = 'registro'), #localhost/registro
    path('inicio', views.InicioView.as_view(), name='inicio'), #localhost/inicio
]