from django import forms
from .models import TiposUnidades, Rutas

Ciudad=[('Ciudad','Ciudad')]
Estado = [('Estado','Estado')] 
Transportista = [('0','Transportista')] 
TipoUnidad = [('0','Tipo Unidad')]
CategoriasEjes = [('0', 'Categoria Ejes')]
Ruta = [('Ruta', 'Ruta')]

class TiposUnidadesForm(forms.Form):
    Nombre = forms.IntegerField(
        widget=forms.Select(choices = TipoUnidad, attrs={
            "class": "form-control"
        })
    )

class TarifaForm(forms.Form):
    IDRuta = forms.IntegerField(
        widget=forms.Select(choices = Ruta, attrs={
            "class": "form-control",
            "onchange" : "buscarRutaG(this);"
        })
    )

    IDTipoUnidad = forms.IntegerField(
        widget=forms.Select(choices = TipoUnidad, attrs={
            "class": "form-control"
        })
    )

    CPOrigen = forms.IntegerField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    CiudadOrigen = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )
    EstadoOrigen = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    CPDestino = forms.IntegerField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    CiudadDestino = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    EstadoDestino = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )
    
    Kilometros = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Kilometros",
            "readonly":"readonly",
            "onkeydown" : "return soloNumeros(this, event);"
        })
    )

    Precio = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Precio",
            "onkeydown" : "return numerosDecimales(this, event);"
        })
    )

    ViajeRedondo = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-contro",
            "placeholder": "Viaje Redondo"
        })
    )

class ActualizarTarifaForm(forms.ModelForm):
    IDRuta = forms.IntegerField(
        widget=forms.Select(choices = Ruta, attrs={
            "class": "form-control",
            "onchange" : "buscarRutaActualizarG(this);"
        })
    )

    IDTipoUnidad = forms.IntegerField(
        widget=forms.Select(choices = TipoUnidad, attrs={
            "class": "form-control"
        })
    )

    CPOrigen = forms.IntegerField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    CiudadOrigen = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    EstadoOrigen = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    CPDestino = forms.IntegerField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    CiudadDestino = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )

    EstadoDestino = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "readonly" :"readonly"
        })
    )
    
    Kilometros = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Kilometros",
            "readonly":"readonly",
            "onkeydown" : "return soloNumeros(this, event);"
        })
    )

    Precio = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Precio",
            "onkeydown" : "return numerosDecimales(this, event);"
        })
    )

    ViajeRedondo = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-contro",
            "placeholder": "Viaje Redondo"
        })
    )

    class Meta:
        model= Rutas
        fields = ('CPOrigen', 'EstadoOrigen', 'CiudadOrigen', 'CPDestino', 'EstadoDestino', 'CiudadDestino', 'Kilometros')

"""
class CrearRutasForm(forms.Form):
    IDTransportista = forms.CharField(
        widget=forms.Select(choices=Transportista, attrs={
            "class": "form-control",
            "onchange":"selectTiposUnidadesTransportista(this);"
        })
    )

    IDTipoUnidad = forms.CharField(
        widget=forms.Select(choices=TipoUnidad, attrs={
            "class": "form-control"
        })
    )

    NombreRuta = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre Ruta",
            "onkeyup" : "mayusculas(this);"
        })
    )

    CPOrigen = forms.IntegerField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "placeholder": "CP Origen",
            "onkeydown" : "return soloNumeros(this, event);",
            "onkeyup" : "buscarEstadoMunicipio(this);",
            'maxlength':"5"
        })
    )

    CiudadOrigen = forms.CharField(
        widget=forms.Select(choices=Ciudad,attrs={
            "class": "form-control",
            "placeholder": "Ciudad Origen"
        })
    )

    EstadoOrigen = forms.CharField(
        widget=forms.Select(choices=Estado, attrs={
            "class": "form-control",
            "placeholder": "Estado Origen"
        })
    )

    CPDestino = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "CP Destino",
            "onkeydown" : "return soloNumeros(this, event);",
            "onkeyup" : "buscarEstadoMunicipioD(this);",
            'maxlength':"5"
        })
    )

    CiudadDestino = forms.CharField(
        widget=forms.Select(choices=Ciudad, attrs={
            "class": "form-control",
            "placeholder": "Ciudad Destino"
        })
    )

    EstadoDestino = forms.CharField(
        widget=forms.Select(choices=Estado, attrs={
            "class": "form-control",
            "placeholder": "Estado Destino"
        })
    )

    Kilometros = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Kilometros",
            "readonly":"readonly",
            "onkeydown" : "return numerosDecimales(this, event);"
        })
    )

    Precio = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Precio",
            "onkeydown" : "return numerosDecimales(this, event);"
        })
    )

    ViajeRedondo = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-contro",
            "placeholder": "Viaje Redondo"
        })
    )
"""
class CrearRutasTForm(forms.Form):
    NombreRuta = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre Ruta",
            "readonly" : "readonly"
        })
    )

    CPOrigen = forms.IntegerField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "placeholder": "CP Origen",
            "onkeydown" : "return soloNumeros(this, event);",
            "onkeyup" : "buscarEstadoMunicipio(this);",
            'maxlength':"5"
        })
    )

    CiudadOrigen = forms.CharField(
        widget=forms.Select(choices=Ciudad,attrs={
            "class": "form-control",
            "placeholder": "Ciudad Origen"
        })
    )

    EstadoOrigen = forms.CharField(
        widget=forms.Select(choices=Estado, attrs={
            "class": "form-control",
            "placeholder": "Estado Origen"
        })
    )

    CPDestino = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "CP Destino",
            "onkeydown" : "return soloNumeros(this, event);",
            "onkeyup" : "buscarEstadoMunicipioD(this);",
            'maxlength':"5"
        })
    )

    CiudadDestino = forms.CharField(
        widget=forms.Select(choices=Ciudad, attrs={
            "class": "form-control",
            "placeholder": "Ciudad Destino"
        })
    )

    EstadoDestino = forms.CharField(
        widget=forms.Select(choices=Estado, attrs={
            "class": "form-control",
            "placeholder": "Estado Destino"
        })
    )

    Kilometros = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Kilometros",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly"
        })
    )

class ActualizarRutasTForm(forms.ModelForm):
    NombreRuta = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre Ruta",
            "readonly":"readonly"
        })
    )

    CPOrigen = forms.IntegerField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "placeholder": "CP Origen",
            "onkeydown" : "return soloNumeros(this, event);",
            "onkeyup" : "buscarEstadoMunicipio(this);",
            'maxlength':"5"
        })
    )

    CiudadOrigen = forms.CharField(
        widget=forms.Select(choices=Ciudad,attrs={
            "class": "form-control",
            "placeholder": "Ciudad Origen"
        })
    )

    EstadoOrigen = forms.CharField(
        widget=forms.Select(choices = Estado,attrs={
            "class": "form-control",
            "placeholder": "Estado Origen"
        })
    )

    CPDestino = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "CP Destino",
            "onkeydown" : "return soloNumeros(this,event);",
            "onkeyup" : "buscarEstadoMunicipioD(this);",
            'maxlength':"5"
        })
    )

    CiudadDestino = forms.CharField(
        widget=forms.Select(choices =Ciudad, attrs={
            "class": "form-control",
            "placeholder": "Ciudad Destino"
        })
    )

    EstadoDestino = forms.CharField(
        widget=forms.Select(choices = Estado, attrs={
            "class": "form-control",
            "placeholder": "Estado Destino"
        })
    )

    Kilometros = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Kilometros",
            "readonly":"readonly",
            "onkeydown" : "return numerosDecimales(this, event);"
        })
    )

    class Meta:
        model= Rutas
        fields = ('NombreRuta', 'CPOrigen', 'CPDestino', 'Kilometros')

class TipoUnidadesEnTiposUnidadesForm(forms.Form):
    Nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return sinEspacios(event)"
        })
    )

    VolumenMax = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return numerosDecimales(this, event)"
        })
    )

    PesoMax = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return numerosDecimales(this, event)"
        })
    )

    Ancho = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return numerosDecimales(this, event)"
        })
    )

    Largo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return numerosDecimales(this, event)"
        })
    )

    IDCategoriaEje = forms.CharField(
        widget=forms.Select(choices=CategoriasEjes, attrs={
            "class": "form-control"
        })
    )

class ActualizarTipoUnidadesEnTiposUnidadesForm(forms.ModelForm):
    Nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return sinEspacios(event)"
        })
    )

    VolumenMax = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return numerosDecimales(this, event)"
        })
    )

    PesoMax = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return numerosDecimales(this, event)"
        })
    )

    Ancho = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return numerosDecimales(this, event)"
        })
    )

    Largo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return numerosDecimales(this, event)"
        })
    )

    IDCategoriaEje = forms.CharField(
        widget=forms.Select(choices=CategoriasEjes, attrs={
            "class": "form-control"
        })
    )

    class Meta:
        model= TiposUnidades
        fields = ('Nombre', 'VolumenMax','PesoMax','Ancho','Largo')
