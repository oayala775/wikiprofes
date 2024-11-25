from django.urls import path
from . import views
from usuario.views import logout_user

app_name = 'publicacion'
urlpatterns = [
    path('', views.PublicacionView.as_view(), name='index'),
    path("profesor/<int:profesor_id>",views.ProfesorView.as_view(), name="profesor"), #'/'
    path("logout",logout_user, name="logout") #'/'
]