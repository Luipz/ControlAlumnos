from django.conf.urls import url
from . import views

urlpatterns = [
    #url('', views.lista_peliculas, name ='lista_peliculas'),
    url('', views.curso_nueva, name='curso_nueva'),
    ]