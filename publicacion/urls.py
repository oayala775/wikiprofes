from django.urls import path
from . import views

app_name = 'publicacion'
urlpatterns = [
    path('profesor/index', views.PublicacionView.as_view(), name='index'),
    path("profesor/<int:profesor_id>",views.ProfesorView.as_view(), name="profesor") #'/'
]