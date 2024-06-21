# En myapp/forms.py

from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'provincia', 'estadio', 'rival']
