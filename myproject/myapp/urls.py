# En myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_equipos, name='lista_equipos'),
    path('agregar/', views.agregar_equipo, name='agregar_equipo'),
     path('borrar/<int:equipo_id>/', views.borrar_equipo, name='borrar_equipo'),
]
