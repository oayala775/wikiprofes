from django.urls import path
from . import views
from usuario.views import logout_user
from .views import PublicacionView, ProfesorView, MateriaView, PublicacionCreateView

app_name = 'publicacion'
urlpatterns = [
    path('', views.PublicacionView.as_view(), name='index'),
    path('crear_reseña', PublicacionCreateView.as_view(), name='crear_reseña'),
    path("profesor/<int:profesor_id>",views.ProfesorView.as_view(), name="profesor"), #'/'
    path("materia/<int:materia_id>",views.MateriaView.as_view(), name="materia"),
    path("logout",logout_user, name="logout") #'/'
   
]