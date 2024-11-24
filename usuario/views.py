from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistroFrom

# enlace entre html y el back-end
class RegistriView(generic.FormView):
    template_name = 'usuario/registro.html'
    form_class = RegistroFrom
    success_url = reverse_lazy('publicacion:index') #cambiar a pagina de inicio del sistema

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        usuario = form.save()
        #el usuario será utilizado para el login en el futuro
        return super().form_valid(form)