from django import forms
from .models import TransportistasProspectos, Prioridades, Estatus, Tipos, Contactos, Certificaciones

Transportistas = [('0', 'Transportista')]
Prioridades = [('0', 'Prioridad')]
Estatus = [('0', 'Estatus')]
Colonias = [('0', 'Colonia')]
Certificacion = [('0', 'Certificacion')]

class TransportistaProspectoForm(forms.Form):
    RazonSocial = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Razon Social"
        })
    )

    NombreComercial = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre Comercial"
        })
    )

    RFC = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "RFC",
            "onkeydown" : "return sinEspacios(event)",
            "onkeyup" : "return mayusculas(this);",
            "maxlength" : "13"
        })
    )
    
    PaginaWeb = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "PaginaWeb",
            "onkeydown" : "return sinEspacios(event)"
        })
    )

    Municipio = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Municipio",
            "readonly":"readonly"
        })
    )

    Estado = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Estado",
            "readonly":"readonly"
        })
    )

    Pais = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Pais",
            "readonly":"readonly"
        })
    )

    CodigoPostal = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "C.P.",
            "onkeyup" : "buscarEstadoMunicipio(this)",
            "onkeydown" : "return soloNumeros(this,event)",
            "maxlength":"5"
        })
    )

    Calle = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Calle"
        })
    )

    NumeroExt = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "#"
        })
    )

    NumeroInt = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "#"
        })
    )

    Colonia = forms.CharField(
        widget=forms.Select(choices = Colonias,attrs={
            "class": "form-control"
        })
    )

    Seguridad = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Seguridad",
            'maxlength':"3",
            "onkeydown":"return soloNumerosEspecial(this,event)"
        })
    )

    PolizaSeguro = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control polizaSeguro",
            "placeholder": "PolizaSeguro"
        })
    )

    Credito = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Dias de Credito",
            "maxlength":"3",
            "onkeydown":"return soloNumerosEspecial(this, event);"
        })
    )

    IDPrioridad = forms.CharField(
        widget=forms.Select(choices = Prioridades,attrs={
            "class": "form-control"
        })
    )


    IDEstatus = forms.CharField(
        widget=forms.Select(choices = Estatus,attrs={
            "class": "form-control",
        })
    )

class ActualizarTransportistaProspectoForm(forms.ModelForm):
    RazonSocial = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Razon Social"
        })
    )

    NombreComercial = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre Comercial"
        })
    )

    RFC = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "RFC",
            "onkeydown" : "return sinEspacios(event)",
            "onkeyup" : "return mayusculas(this);",
            "maxlength" : "13"
        })
    )
    
    PaginaWeb = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "PaginaWeb",
            "onkeydown" : "return sinEspacios(event)"
        })
    )

    Municipio = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Municipio",
            "readonly":"readonly"
        })
    )

    Estado = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Estado",
            "readonly":"readonly"
        })
    )

    Pais = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Pais",
            "readonly":"readonly"
        })
    )

    CodigoPostal = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "C.P.",
            "onkeyup" : "buscarEstadoMunicipio(this)",
            "onkeydown" : "return soloNumeros(this,event)",
            "maxlength":"5"
        })
    )

    Calle = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Calle"
        })
    )

    NumeroExt = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "#"
        })
    )

    NumeroInt = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "#"
        })
    )

    Colonia = forms.CharField(
        widget=forms.Select(choices = Colonias,attrs={
            "class": "form-control"
        })
    )

    Seguridad = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Seguridad",
            'maxlength':"3",
            "onkeydown":"return soloNumerosEspecial(this,event)"
        })
    )

    PolizaSeguro = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "PolizaSeguro"
        })
    )

    Credito = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Dias de Credito",
            "maxlength":"3",
            "onkeydown":"return soloNumerosEspecial(this, event);"
        })
    )

    IDPrioridad = forms.CharField(
        widget=forms.Select(choices = Prioridades,attrs={
            "class": "form-control"
        })
    )


    IDEstatus = forms.CharField(
        widget=forms.Select(choices = Estatus,attrs={
            "class": "form-control"
        })
    )

    class Meta:
        model = TransportistasProspectos
        fields = ('RazonSocial', 'NombreComercial', 'RFC', 'PaginaWeb', 'Municipio', 'Estado', 'Pais', 'CodigoPostal',
        'Calle', 'NumeroExt', 'NumeroInt', 'Colonia', 'Seguridad', 'PolizaSeguro', 'Credito', 'IDPrioridad', 'IDEstatus')

class CertificacionesForm(forms.Form):
    Nombre = forms.CharField(
        widget=forms.Select(choices = Certificacion, attrs={
            "class": "form-control"
        })
    )

class ContactosForm(forms.Form):
    Profesion = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Profesion"
        })
    )

    NombreIFE = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre IFE"
        })
    )

    PrimerNombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Primer Nombre"
        })
    )

    SegundoNombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Segundo Nombre"
        })
    )

    ApellidoPaterno = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apellido Paterno"
        })
    )

    ApellidoMaterno = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apellido Materno"
        })
    )

    Puesto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Puesto"
        })
    )

    Telefono = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Telefono",
            'maxlength':"15",
            "onkeydown":"return soloNumeros(this, event);"
        })
    )

    Correo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "@",
            "onkeydown" : "return sinEspacios(event);"
        })
    )

    CorreoAdicional = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "@",
            "onkeydown" : "return sinEspacios(event);"
        })
    )

class ActualizarContactosForm(forms.ModelForm):
    Profesion = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Profesion"
        })
    )

    NombreIFE = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre IFE"
        })
    )

    PrimerNombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Primer Nombre"
        })
    )

    SegundoNombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Segundo Nombre"
        })
    )

    ApellidoPaterno = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apellido Paterno"
        })
    )

    ApellidoMaterno = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apellido Materno"
        })
    )

    Puesto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Puesto"
        })
    )

    Telefono = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Telefono",
            'maxlength':"10",
            "onkeydown":"return soloNumeros(this, event);"
        })
    )

    Correo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "@",
            "onkeydown" : "return sinEspacios(event);"
        })
    )

    CorreoAdicional = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "@",
            "onkeydown" : "return sinEspacios(event);"
        })
    )

    class Meta:
        model = Contactos
        fields = ('Profesion', 'NombreIFE', 'PrimerNombre', 'SegundoNombre', 'ApellidoPaterno', 'ApellidoMaterno', 
                    'Puesto', 'Telefono', 'Correo', 'CorreoAdicional')

class ContactosEnContactosForm(forms.Form):
    IDTransportista = forms.CharField(
        widget=forms.Select(choices = Transportistas,attrs={
            "class": "form-control",
        })
    )

    Profesion = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Profesion"
        })
    )

    NombreIFE = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre IFE"
        })
    )

    PrimerNombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Primer Nombre"
        })
    )

    SegundoNombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Segundo Nombre"
        })
    )

    ApellidoPaterno = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apellido Paterno"
        })
    )

    ApellidoMaterno = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apellido Materno"
        })
    )

    Puesto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Puesto"
        })
    )

    Telefono = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Telefono",
            'maxlength':"15",
            "onkeydown":"return soloNumeros(this, event);"
        })
    )

    Correo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "@",
            "onkeydown" : "return sinEspacios(event);"
        })
    )

    CorreoAdicional = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "@",
            "onkeydown" : "return sinEspacios(event);"
        })
    )

class CertificacionesEnCertificacionesForm(forms.Form):
    Nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return sinEspacios(event)"
        })
    )

class ActualizarCertificacionesEnCertificacionesForm(forms.ModelForm):
    Nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "onkeydown" : "return sinEspacios(event)"
        })
    )

    class Meta:
        model = Certificaciones
        fields = ('Nombre',)
