from django.urls import path
from . import views

app_name = 'publicacion'
urlpatterns = [
    path('', views.PublicacionView.as_view(), name='index') #'/'
]