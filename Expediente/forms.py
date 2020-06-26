from django import forms
from Expediente.models import Expediente, Extras, Bitacora
from django.core.validators import ValidationError

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('FormatoAlta', 'ActaConstitutiva', 'CedulaFiscal', 'IFERepresentante',
                  'ComprobanteDomicilio', 'CaratulaBancaria', 'ConvenioConfidencialidad',
                  'ContratoServicios', 'ConvenioTarifas', 'Descripcion', 'Permisos', 'Licencias',)


class ExpedienteFAltaForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('FormatoAlta',)
        labels = {
            "FormatoAlta": "Formato Alta",
        }


class ExpedienteActaConsti(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('ActaConstitutiva',)
        labels = {
            "ActaConstitutiva": "Acta Constitutiva",
        }


class ExpedienteCedFis(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('CedulaFiscal',)
        labels = {
            "CedulaFiscal": "Cedula Fiscal",
        }


class ExpedienteIFE(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('IFERepresentante',)
        labels = {
            "IFERepresentante": "IFE Representante",
        }


class ExpedienteComDom(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('ComprobanteDomicilio',)
        labels = {
            "ComprobanteDomicilio": "Comprobante Domicilio",
        }


class ExpedienteCarBan(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('CaratulaBancaria',)
        labels = {
            "CaratulaBancaria": "Caratula Bancaria",
        }


class ExpedienteConCon(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('ConvenioConfidencialidad',)
        labels = {
            "ConvenioConfidencialidad": "Convenio Confidencialidad",
        }


class ExpedienteConSer(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('ContratoServicios',)
        labels = {
            "ContratoServicios": "Contrato Servicios",
        }


class ExpedienteConTar(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('ConvenioTarifas',)
        labels = {
            "ConvenioTarifas": "Convenio Tarifas",
        }


class ExpedienteDes(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('Descripcion',)
        labels = {
            "Descripcion": "Descripcion",
        }


class ExpedientePer(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('Permisos',)
        labels = {
            "Permisos": "Permisos",
        }


class ExpedienteLic(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('Licencias',)
        labels = {
            "Licencias": "Licencias",
        }


class ExtrasForm(forms.ModelForm):
    class Meta:
        model = Extras
        fields = ('Image',)
        labels = {
            "Image": "Logo",
        }


class TarjetaDirForm(forms.ModelForm):
    class Meta:
        model = Extras
        fields = ('TarjetaDirector',)
        labels = {
            "TarjetaDirector": "Tarjeta Director",
        }


class TarjetaVentForm(forms.ModelForm):
    class Meta:
        model = Extras
        fields = ('TarjetaVentas',)
        labels = {
            "TarjetaVentas": "Tarjeta Ventas",
        }


class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = ('Fecha', 'RepLGK', 'RepTransportista')
        widgets = {
            'Fecha': forms.DateTimeInput(attrs={'class': 'datetime-input', "type": "date"})
        }