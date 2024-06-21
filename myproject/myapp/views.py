# En myapp/views.py

from django.shortcuts import render, redirect
from .models import Equipo
from .forms import EquipoForm

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'index.html', {'equipos': equipos})

def agregar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')  # Redirige a la página de lista de equipos
    else:
        form = EquipoForm()
    
    return render(request, 'agregar_equipo.html', {'form': form})

def borrar_equipo(request, equipo_id):
    equipo = Equipo.objects.get(pk=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('lista_equipos')
    return render(request, 'borrar_equipo.html', {'equipo': equipo})