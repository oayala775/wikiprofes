from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()


    def clean_username(self):
        usuario = self.cleaned_data.get("username")
        if User.objects.filter(username=usuario):
            raise forms.ValidationError("El usuario ya fue registrado anteriormente.")
        return usuario

    def clean_email(self):
        correo = self.cleaned_data.get("email")
        if "@alumnos.udg.mx" not in correo:
            raise forms.ValidationError("El correo no pertenece a la Universidad de Guadalajara.")
        return correo

    def clean(self):
        datos = self.cleaned_data
        password1 = datos.get("password") 
        password2 = datos.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return datos

    def save(self):
        self.cleaned_data.pop("password2")
        return User.objects.create_user(**self.cleaned_data)
    
