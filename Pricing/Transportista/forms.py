from django import forms
from Transportista.models import Transportista, Expediente, Extras, Bitacora, Unidad, UnidadType, Tarifas, Remolque
from django.core.validators import ValidationError

CHOICES = [('', 'Colonia')]
CHOICESTipos = [('Paquetería', 'Paquetería'), ('Carga seca', 'Carga seca'),
                ('Productos precederos', 'Productos precederos'),
                ('Material pesado a granel ', 'Material pesado a granel '),
                ('líquidos', 'líquidos'), ('Gases', 'Gases'),
                ('Productos químicos y petroquímicos', 'Productos químicos y petroquímicos'),
                ('Productos alimenticios a granel', 'Productos alimenticios a granel'),
                ('Animales varios', 'Animales varios'),
                ('Maquinaria o productos pesados', 'Maquinaria o productos pesados'),
                ('Carga a granel', 'Carga a granel'), ('Material para construcción', 'Material para construcción'),
                ('Vehículos', 'Vehículos'), ]


class TransportistaForm(forms.Form):
    RazonSocial = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control razonSocial",
            "placeholder": "Razon Social"
        })
    )
    Email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class": "form-control email",
            "placeholder": "Email"
        })
    )
    NombreComercial = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control nombreComercial",
            "placeholder": "Nombre Comercial"
        })
    )
    NombreContacto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control nombreContacto",
            "placeholder": "Nombre del Contacto"
        })
    )
    Calle = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control calle",
            "placeholder": "Calle"
        })
    )
    NumInt = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control numInt",
                                 "placeholder": "numInt"
                             })
                             )
    NumExt = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control numExt",
                                 "placeholder": "numExt"
                             })
                             )
    Estado = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control estado",
            "placeholder": "Estado"
        })
    )
    Ciudad = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control ciudad",
            "placeholder": "Ciudad"
        })
    )
    CP = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control CP",
            "placeholder": "C.P."
        })
    )
    Colonia = forms.CharField(
        widget=forms.Select(choices=CHOICES, attrs={
            "class": "form-control Colonia",
            "placeholder": "Colonia"
        })
    )
    BaseTerminal = forms.CharField(required=False,
                                   widget=forms.TextInput(attrs={
                                       "class": "form-control baseTerminal",
                                       "placeholder": "Terminal/Base"
                                   })
                                   )
    Telefonos = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control telefonos",
            "placeholder": "Telefono"
        })
    )
    PaginaWeb = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={
                                    "class": "form-control PaginaWeb",
                                    "placeholder": "PaginaWeb"
                                })
                                )
    Credito = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control Credito",
            "placeholder": "Dias de Credito"
        })
    )

    def clean_email(self):
        Email = self.cleaned_data['Email']
        if Transportista.objects.filter(Email=Email).exists():
            raise ValidationError("El correo ya existe")
        return Email


class AddRutasForm(forms.Form):
    IDRutas = forms.IntegerField(
        widget=forms.Select(choices=CHOICES, attrs={
            "class": "form-control Carrier",
            "placeholder": "Carrier"
        })
    )


class UpTransportistaForm(forms.ModelForm):
    RazonSocial = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control razonSocial",
            "placeholder": "Razon Social"
        })
    )
    Email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class": "form-control email",
            "placeholder": "Email"
        })
    )
    NombreComercial = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control nombreComercial",
            "placeholder": "Nombre Comercial"
        })
    )
    NombreContacto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control nombreContacto",
            "placeholder": "Nombre del Contacto"
        })
    )
    Calle = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control calle",
            "placeholder": "Calle"
        })
    )
    NumInt = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control numInt",
                                 "placeholder": "numInt"
                             })
                             )
    NumExt = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control numExt",
                                 "placeholder": "numExt"
                             })
                             )
    Estado = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control estado",
            "placeholder": "Estado"
        })
    )
    Ciudad = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control ciudad",
            "placeholder": "Ciudad"
        })
    )
    CP = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control CP",
            "placeholder": "C.P."
        })
    )
    Colonia = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control Colonia",
            "placeholder": "Colonia"
        })
    )
    BaseTerminal = forms.CharField(required=False,
                                   widget=forms.TextInput(attrs={
                                       "class": "form-control baseTerminal",
                                       "placeholder": "Terminal/Base"
                                   })
                                   )
    Telefonos = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control telefonos",
            "placeholder": "Telefono"
        })
    )
    PaginaWeb = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={
                                    "class": "form-control PaginaWeb",
                                    "placeholder": "PaginaWeb"
                                })
                                )
    Credito = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control Credito",
            "placeholder": "Dias de Credito"
        })
    )

    class Meta:
        model = Transportista
        fields = ('RazonSocial', 'Email', 'NombreComercial', 'NombreContacto', 'Calle', 'NumInt',
                  'NumExt', 'Estado', 'Ciudad', 'CP', 'Colonia', 'BaseTerminal', 'Telefonos', 'PaginaWeb', 'Credito')


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


class UnidadesForm(forms.ModelForm):
    IDUnitType = forms.IntegerField(
        widget=forms.Select(choices=CHOICES, attrs={
            "class": "form-control tipoUnidad",
            "placeholder": "Tipo Unidad"
        })
    )
    IDTransportista = forms.IntegerField(
        widget=forms.Select(choices=CHOICES, attrs={
            "class": "form-control transportista",
            "placeholder": "Transportista"
        })
    )
    Nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control nombre",
            "placeholder": "Nombre"
        })
    )
    Combustible = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control combustible",
            "placeholder": "Combustible"
        })
    )
    Performance = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control Performance",
            "placeholder": "Performance"
        })
    )
    RegistroVehiculo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control registroVehiculo",
            "placeholder": "Registro Vehiculo"
        })
    )
    FechaExpiracion = forms.DateField(
        widget=forms.DateInput(attrs={
            "class": "datetime-input",
            "type": "date",
            "placeholder": "Fecha Expiracion"
        })
    )
    Marca = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control marca",
            "placeholder": "Marca"
        })
    )
    Modelo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control modelo",
            "placeholder": "Modelo"
        })
    )
    Anno = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control anno",
            "placeholder": "Año"
        })
    )
    Placas = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control placas",
                                 "placeholder": "Placas"
                             }), error_messages={'required': 'Please choose a star rating'}
                             )
    Econnum = forms.IntegerField(required=False,
                                 widget=forms.NumberInput(attrs={
                                     "class": "form-control Econnum",
                                     "placeholder": "Econnum"
                                 })
                                 )
    NumeroSatelital = forms.IntegerField(required=False,
                                         widget=forms.NumberInput(attrs={
                                             "class": "form-control numeroSatelital",
                                             "placeholder": "Numero Satelital"
                                         })
                                         )
    Special = forms.BooleanField(required=False,
                                 widget=forms.CheckboxInput(attrs={
                                     "class": "form-control special",
                                     "placeholder": "Special"
                                 })
                                 )
    FullUnit = forms.BooleanField(required=False,
                                  widget=forms.CheckboxInput(attrs={
                                      "class": "form-control fullUnit",
                                      "placeholder": "FullUnit"
                                  })
                                  )

    class Meta:
        model = Unidad
        fields = (
        'Nombre', 'Combustible', 'Performance', 'RegistroVehiculo', 'RegistroTarjeta', 'FechaExpiracion', 'Marca',
        'Modelo', 'Anno', 'Placas', 'Econnum', 'NumeroSatelital', 'PlacasTraseras', 'Seguro', 'Special', 'FullUnit')


class registroTarjetaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(registroTarjetaForm, self).__init__(*args, **kwargs)
        self.fields['RegistroTarjeta'].label = False

    class Meta:
        model = Unidad
        fields = ('RegistroTarjeta',)


class placasTraserasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(placasTraserasForm, self).__init__(*args, **kwargs)
        self.fields['PlacasTraseras'].label = False

    class Meta:
        model = Unidad
        fields = ('PlacasTraseras',)


class seguroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(seguroForm, self).__init__(*args, **kwargs)
        self.fields['Seguro'].label = False

    class Meta:
        model = Unidad
        fields = ('Seguro',)


class UnidadTypeForm(forms.ModelForm):
    Nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control nombre",
            "placeholder": "Nombre"
        })
    )
    Capacidad = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control capacidad",
            "placeholder": "Capacidad (Ton)"
        })
    )
    Medidas = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control medidas",
            "placeholder": "Medidas"
        })
    )
    Configuraciones = forms.MultipleChoiceField(required=False,choices=CHOICESTipos,
                                                widget=forms.CheckboxSelectMultiple(attrs={
                                                    "placeholder": "Configuraciones"
                                                })
                                                )

    def __init__(self, *args, **kwargs):
        super(UnidadTypeForm, self).__init__(*args, **kwargs)
        self.fields['Image'].label = False

    class Meta:
        model = UnidadType
        fields = ('Nombre', 'Capacidad', 'Medidas', 'Configuraciones', 'Image',)


class TarifasForm(forms.ModelForm):
    Equipo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control equipo",
            "placeholder": "Equipo"
        })
    )
    Origen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control origen",
            "placeholder": "Origen"
        })
    )
    Tarifa = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control tarifa",
            "placeholder": "Tarifa"
        })
    )
    Destino = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control destino",
            "placeholder": "Destino"
        })
    )
    Moneda = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control moneda",
            "placeholder": "Moneda"
        })
    )
    Comentarios = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control comentarios",
            "placeholder": "Comentarios"
        })
    )

    def __init__(self, *args, **kwargs):
        super(TarifasForm, self).__init__(*args, **kwargs)
        self.fields['Evidencia'].label = False

    class Meta:
        model = Tarifas
        fields = ('Equipo', 'Origen', 'Destino', 'Moneda', 'Comentarios', 'Evidencia',)


class RemolqueForm(forms.ModelForm):
    IDUnitType = forms.IntegerField(
        widget=forms.Select(choices=CHOICES, attrs={
            "class": "form-control tipoUnidad",
            "placeholder": "Tipo Unidad"
        })
    )
    IDTransportista = forms.IntegerField(
        widget=forms.Select(choices=CHOICES, attrs={
            "class": "form-control transportista",
            "placeholder": "Transportista"
        })
    )
    Nombre = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control nombre",
                                 "placeholder": "Nombre"
                             })
                             )
    Marca = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={
                                "class": "form-control marca",
                                "placeholder": "Marca"
                            })
                            )
    Modelo = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control modelo",
                                 "placeholder": "Modelo"
                             })
                             )
    Anno = forms.IntegerField(required=False,
                              widget=forms.NumberInput(attrs={
                                  "class": "form-control anno",
                                  "placeholder": "Año"
                              })
                              )
    Placas = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control placas",
                                 "placeholder": "Placas"
                             })
                             )
    Econnum = forms.CharField(required=False,
                              widget=forms.TextInput(attrs={
                                  "class": "form-control econnum",
                                  "placeholder": "Econnum"
                              })
                              )
    NumeroSatelital = forms.IntegerField(required=False,
                                         widget=forms.NumberInput(attrs={
                                             "class": "form-control numeroSatelital",
                                             "placeholder": "Numero Satelital"
                                         })
                                         )
    Volumen = forms.IntegerField(required=False,
                                 widget=forms.NumberInput(attrs={
                                     "class": "form-control volumen",
                                     "placeholder": "Volumen"
                                 })
                                 )
    Peso = forms.IntegerField(required=False,
                              widget=forms.NumberInput(attrs={
                                  "class": "form-control peso",
                                  "placeholder": "Peso"
                              })
                              )
    Longitud = forms.IntegerField(required=False,
                                  widget=forms.NumberInput(attrs={
                                      "class": "form-control longitud",
                                      "placeholder": "Longitud"
                                  })
                                  )
    Ancho = forms.IntegerField(required=False,
                               widget=forms.NumberInput(attrs={
                                   "class": "form-control ancho",
                                   "placeholder": "Ancho"
                               })
                               )

    class Meta:
        model = Remolque
        fields = (
        'Nombre', 'Marca', 'Modelo', 'Anno', 'Placas', 'Econnum', 'NumeroSatelital', 'Volumen', 'Peso', 'Longitud',
        'Ancho', 'PlacasTraseras', 'Seguro', 'FacturaRemolque')
