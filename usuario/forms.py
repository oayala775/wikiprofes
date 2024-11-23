#vamos a recibir y validar los datos que vienen del front
from typing import Any
from django import forms
from django.contrib.auth.models import User

class RegistroFrom(forms.Form):
    #variables en las que recibiremos datos del front
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()

    #validar usuarios
    def clean_username(self):
         #adquirimos el valor del formulario
        usuario = self.cleaned_data.get('username')
        #comprobamos que el usuarios no este registrado
        if User.objects.filter(username = usuario):
            #mandamos error
            raise forms.ValidationError('Nombre de usuario no disponible')
        return usuario
    
    def clean_email(self):
        correo = self.cleaned_data.get('email')
        if '@alumnos.udg.mx' not in correo:
            raise forms.ValidationError('Correo no válido')
        return correo
    
    #validacion generica
    def clean(self):
        datos = self.cleaned_data
        password_1 = datos.get('password')
        password_2 = datos.get('password2')
        if password_1 != password_2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return datos
    
    #guardar en la base de datos
    def save(self):
        self.cleaned_data.pop('password2')
        return User.objects.create_user(**self.cleaned_data)

