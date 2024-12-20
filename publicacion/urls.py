from django.urls import path
from . import views
from usuario.views import logout_user

app_name = 'publicacion'
urlpatterns = [
    path('', views.PublicacionView.as_view(), name='index'),
    path('crear_reseña', views.PublicacionCreateView.as_view(), name='crear_reseña'),
    path("profesor/<int:profesor_id>",views.ProfesorView.as_view(), name="profesor"), #'/'
    path("materia/<int:materia_id>",views.MateriaView.as_view(), name="materia"),
    path("busqueda_materia/<str:materia_nombre>",views.BusquedaMateriaView.as_view(), name="busqueda_materia"),
    path("busqueda_profesor/<str:profesor_nombre>",views.BusquedaProfesorView.as_view(), name="busqueda_profesor"),
    path("logout",logout_user, name="logout") #'/'
   
]