from django.urls import path
from . import views

#Establecer vistas y url correspondiente
app_name = 'usuario'
urlpatterns = [
    path('registro', views.RegistroView.as_view(), name = 'registro')
]