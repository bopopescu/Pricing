from django import forms
from Availability.models import EquipoDisponible
from django.core.validators import ValidationError

CHOICES=[('','Select')]

class availabilityForm(forms.ModelForm):
    Carrier = forms.IntegerField(
        widget=forms.Select(choices=CHOICES,attrs={
            "class": "form-control transportista",
            "placeholder": "Carrier"
        })
    )
    Rutas = forms.IntegerField(
        widget=forms.Select(choices=CHOICES,attrs={
            "class": "form-control Rutas",
            "placeholder": "Rutas"
        })
    )
    NoUnidades = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control NoUnidades",
            "placeholder": "No. Unidades"
        })
    )
    class Meta:
        model= EquipoDisponible
        fields = ('NoUnidades',)

class availabilityUpdateForm(forms.ModelForm):
    NoUnidades = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control NoUnidades",
            "placeholder": "No. Unidades"
        })
    )
    class Meta:
        model= EquipoDisponible
        fields = ('NoUnidades',)

class availabilityDisponibilidadform(forms.ModelForm):
    Disponibles = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control Disponibles",
            "placeholder": "Disponibles"
        })
    )
    Ocupado = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control Ocupado",
            "placeholder": "Ocupado"
        })
    )
    class Meta:
        model= EquipoDisponible
        fields = ()