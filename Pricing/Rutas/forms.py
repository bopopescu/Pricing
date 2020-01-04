from django import forms
from Rutas.models import Rutas
from django.core.validators import ValidationError
CHOICES=[('','Colonia')]
class RutasForm(forms.Form):
    CPOrigen = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control CPOrigen",
            "placeholder": "CP Origen"
        })
    )
    CiudadOrigen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control CiudadOrigen",
            "placeholder": "Ciudad Origen"
        })
    )
    EstadoOrigen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control EstadoOrigen",
            "placeholder": "Estado Origen"
        })
    )
    CPDestino = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control CPDestino",
            "placeholder": "CP Destino"
        })
    )
    CiudadDestino = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control CiudadDestino",
            "placeholder": "Ciudad Destino"
        })
    )
    EstadoDestino = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control EstadoDestino",
            "placeholder": "Estado Destino"
        })
    )
    ViajeRedondo = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-control viajeRedondo",
            "placeholder": "Viaje Redondo"
        })
    )
    NombreRuta = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control NombreRuta",
            "placeholder": "Nombre Ruta"
        })
    )
    Kilometros = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control Kilometros",
            "placeholder": "Kilometros"
        })
    )
    Casetas = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control Casetas",
            "placeholder": "Casetas"
        })
    )

class RutasUpForm(forms.ModelForm):
    CPOrigen = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control CPOrigen",
            "placeholder": "CP Origen"
        })
    )
    CiudadOrigen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control CiudadOrigen",
            "placeholder": "Ciudad Origen"
        })
    )
    EstadoOrigen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control EstadoOrigen",
            "placeholder": "Estado Origen"
        })
    )
    CPDestino = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control CPDestino",
            "placeholder": "CP Destino"
        })
    )
    CiudadDestino = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control CiudadDestino",
            "placeholder": "Ciudad Destino"
        })
    )
    EstadoDestino = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control EstadoDestino",
            "placeholder": "Estado Destino"
        })
    )
    NombreRuta = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control NombreRuta",
            "placeholder": "Nombre Ruta"
        })
    )
    Kilometros = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control Kilometros",
            "placeholder": "Kilometros"
        })
    )
    Casetas = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control casetas",
            "placeholder": "Casetas"
        })
    )
    class Meta:
        model= Rutas
        fields = ('CPOrigen', 'CiudadOrigen', 'EstadoOrigen', 'CPDestino', 'CiudadDestino', 'EstadoDestino', 'NombreRuta', 'Kilometros')