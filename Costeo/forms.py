from django import forms
from Costeo.models import Depreciacion, FactoresPremisas, CostosOperativos, Costeo

CHOICES=[('','Select')]
RUTAS = [('Ruta', 'Ruta')]
TIPOSUNIDADES = [('Tipo Unidad', 'Tipo Unidad')]
MODELOS = [('0', 'Modelo')]

class DepreciacionForm(forms.ModelForm):
    Meses = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control meses",
            "placeholder": "Meses"
        })
    )
    CostosUnidad = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control costosUnidad",
            "placeholder": "Costos Unidad"
        })
    )
    CostosCaja = forms.DecimalField(
    	widget=forms.NumberInput(attrs={
    		"class" : "form-control costosCaja",
    		"placeholder" : "Costos Caja"
    	})
    )
    ViajesMes = forms.IntegerField(
    	widget=forms.NumberInput(attrs={
    		"class" : "form-control viajeMes",
    		"placeholder" : "Viajes al mes"
    	})
    )
    KmsMesXunidad = forms.DecimalField(
    	widget=forms.NumberInput(attrs={
    		"class" : "form-control viajeMes",
    		"placeholder" : "Kms al mes por unidad"
    	})
    )
    DepTracto = forms.DecimalField(
    	widget=forms.NumberInput(attrs={
    		"class" : "form-control depTracto",
    		"placeholder" : "Dep Tracto"
    	})
    )
    DepCaja = forms.DecimalField(
    	widget=forms.NumberInput(attrs={
    		"class" : "forms-control depTracto",
    		"placeholder" : "Dep Caja"
    	})
    )
    RentaGps = forms.DecimalField(
    	widget=forms.NumberInput(attrs={
    		"class" : "forms-control rentaGps",
    		"placeholder" : "Renta GPS"
    	})
    )
    PlacasTenencia = forms.DecimalField(
    	widget=forms.NumberInput(attrs={
    		"class" : "forms-control placasTenencia",
    		"placeholder" : "Placas Tenecia"
    	})
    )
    Seguro = forms.DecimalField(
    	widget=forms.NumberInput(attrs={
    		"class" : "forms-control seguro",
    		"placeholder" : "Seguro"
    	})
    )
    Admvo = forms.IntegerField(
    	widget=forms.NumberInput(attrs={
    		"class" : "forms-control admvo",
    		"placeholder" : "admvo"
    	})
    )
    Financieros = forms.IntegerField(
    	widget=forms.NumberInput(attrs={
    		"class" : "forms-control financieros",
    		"placeholder" : "Financieros"
    	})
    )
    MttoUnidadXkm = forms.DecimalField(
    	widget=forms.NumberInput(attrs={
    		"class" : "forms-control mttoUnidadXkm",
    		"placeholder" : "Mtto unidad por km"
    	})
	)
    Llantas = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "forms-control llantas",
            "placeholder" : "Llantas"
        })
    )
    Operador = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "forms-control operador",
            "placeholder" : "Operador"
        })
    )
    DobleOp = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "forms-control dobleOp",
            "placeholder" : "Doble Operador"
        })
    )
    class Meta:
        model = Depreciacion
        fields = ('Meses', 'CostosUnidad', 'CostosCaja', 'ViajesMes', 'KmsMesXunidad', 'DepTracto', 'DepCaja','RentaGPS', 'PlacasTenencia', 'Seguro', 'Admvo', 'Financieros', 'MttoUnidadXkm', 'Llantas', 'Operador', 'DobleOp')

class FactoresPremisasForm(forms.ModelForm):
    Unidad = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control unidad",
            "placeholder": "Unidad"
        })
    )
    Caja = forms.IntegerField(
        widget=forms.NumberInput(attrs={
        "class" : "form-control unidad",
        "placeholder" : "Caja"
        })
    )
    KmSencillo = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control kmSencillo",
            "placeholder": "Km sencillo"
        })
    )
    KmRoundTrip = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control kmRoundTrip",
            "placeholder" : "Km RoundTrip"
        })
    )
    casetasSingle = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control casetasSingle",
            "placeholder" : "Casetas Single"
        })
    )
    Rendimiento = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control rendimiento",
            "placeholder" : "Rendimiento"
        })
    )
    Diesel = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control diesel",
            "placeholder" : "Diesel"
        })
    )
    DieselSinIva = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control dieselSinIva",
            "placeholder" : "Diesel Sin Iva"
        })
    )
    class Meta:
        model = FactoresPremisas
        fields = ('Unidad', 'Caja', 'KmSencillo', 'KmRoundTrip', 'CasetaSingle', 'Rendimiento', 'Diesel', 'DieselSinIva')

class DirectoVariebleForm(forms.ModelForm):
    Combustible = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control combustible",
            "placeholder": "Combustible"
        })
    )
    Casetas = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control casetas",
            "placeholder": "Casetas"
        })
    )
    Operador = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control operador",
            "placeholder": "Operador"
        })
    )
    Subtotal1 = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control subtotal1",
            "placeholder": "Subtotal"
        })
    )
    class Meta:
        model = CostosOperativos
        fields = ('Combustible', 'Casetas', 'Operador', 'Subtotal1')

class IndirectoFijoForm(forms.ModelForm):
    MttoUnidad = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control mttoUnidad",
            "placeholder": "Mtto Unidad"
        })
    )
    LlantasUnidad = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control llantasUnidad",
            "placeholder": "Llantas Unidad"
        })
    )
    Gps = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control gps",
            "placeholder": "GPS"
        })
    )
    Seguro = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control seguro",
            "placeholder": "seguro"
        })
    )
    PlacasTenencia = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control placasTenencia",
            "placeholder": "Placas Tenencia"
        })
    )
    SubTotal2 = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control subTotal2",
            "placeholder": "SubTotal"
        })
    )
    class Meta:
        model = CostosOperativos
        fields = ('MttoUnidad', 'LlantasUnidad', 'Gps', 'Seguro', 'PlacasTenencia', 'SubTotal2')

class AdmvoFinancieroForm(forms.ModelForm):
    Admvo = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control admvo",
            "placeholder" : "Admvo"
        })
    )
    Financieros = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control financieros",
            "placeholder" : "Finacieros"
        })
    )
    DeprUnidad = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control deprUnidad",
            "placeholder" : "Depr. Unidad"
        })
    )
    DeprRemolque = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control deprRemolque",
            "placeholder" : "Depr. Remolque"
        })
    )
    Subtotal3 = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control subtotal3",
            "placeholder" : "Subtotal"
        })
    )
    class Meta:
        model = CostosOperativos
        fields = ('Admvo', 'Financieros', 'DeprUnidad', 'DeprRemolque', 'Subtotal3')

class CosteoForm(forms.Form):
    Empresa = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control"
        })
    )

    IDRuta = forms.IntegerField(
        widget=forms.Select(choices=RUTAS,attrs={
            "class": "form-control",
            "onchange" : "buscarRutaCosto(this);"
        })
    )

    Kilometros = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Kilometros",
            "onkeydown" : "return soloNumeros(this, event);",
            "readonly" : "readonly"
        })
    )

    CiudadOrigen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ciudad Origen",
            "readonly" : "readonly" 
        })
    )

    EstadoOrigen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Estado Origen",
            "readonly" : "readonly" 
        })
    )

    CPOrigen = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "placeholder": "CP Origen",
            'maxlength':"5"
        })
    )

    CiudadDestino = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ciudad Destino",
            "readonly" : "readonly" 
        })
    )

    EstadoDestino = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Estado Destino",
            "readonly" : "readonly" 
        })
    )

    CPDestino = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "CP Destino",
            'maxlength':"5"
        })
    )

    IDTipoUnidad= forms.IntegerField(
        widget=forms.Select(choices=TIPOSUNIDADES,attrs={
            "class": "form-control",
            "placeholder": "Tipo Unidad",
            "onchange" : "procedimiento();"
        })
    )

    IDModelo = forms.IntegerField(
        widget=forms.Select(choices=MODELOS,attrs={
            "class": "form-control",
            "placeholder": "Modelos",
            "onchange":"unidadCaja();"
        })
    )

    Casetas = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Casetas",
            "onkeydown" : "return numerosDecimales(this, event);"
        })
    )

    Producto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control producto",
            "placeholder": "Producto"
        })
    )

    ViajeRedondo = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-contro",
            "placeholder": "Viaje"
        })
    )

    TotalCostos = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Total Costos",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly" 
        })
    )

    FactorAjustePor = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "%",
            "onkeydown" : "return numerosDecimales100(this, event);",
        })
    )

    FactorAjuste = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Factor Ajuste",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly"
        })
    )

    MopPor = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "%",
            "onkeydown" : "return numerosDecimales100(this, event);",
        })
    )

    Mop = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Mop",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly"
        })
    )

    TotalTransportista = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Total Transportista",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly" 
        })
    )

class CosteoActualizarForm(forms.ModelForm):
    Empresa = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control"
        })
    )

    IDRuta = forms.IntegerField(
        widget=forms.Select(choices=RUTAS,attrs={
            "class": "form-control",
            "onchange" : "buscarRutaCostoActualizar(this);"
        })
    )

    Kilometros = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Kilometros",
            "onkeydown" : "return soloNumeros(this, event);",
            "readonly" : "readonly"
        })
    )

    CiudadOrigen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ciudad Origen",
            "readonly" : "readonly" 
        })
    )

    EstadoOrigen = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Estado Origen",
            "readonly" : "readonly" 
        })
    )

    CPOrigen = forms.CharField(
        widget=forms.TextInput( attrs={
            "class": "form-control",
            "placeholder": "CP Origen",
            'maxlength':"5"
        })
    )

    CiudadDestino = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ciudad Destino",
            "readonly" : "readonly" 
        })
    )

    EstadoDestino = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Estado Destino",
            "readonly" : "readonly" 
        })
    )

    CPDestino = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "CP Destino",
            'maxlength':"5"
        })
    )

    IDTipoUnidad= forms.IntegerField(
        widget=forms.Select(choices=TIPOSUNIDADES,attrs={
            "class": "form-control",
            "placeholder": "Tipo Unidad",
            "onchange" : "procedimientoActualizar();"
        })
    )

    IDModelo = forms.IntegerField(
        widget=forms.Select(choices=MODELOS,attrs={
            "class": "form-control",
            "placeholder": "Modelos",
            "onchange":"unidadCaja();"
        })
    )

    Casetas = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Casetas",
            "onkeydown" : "return numerosDecimales(this, event);"
        })
    )

    Producto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control producto",
            "placeholder": "Producto"
        })
    )

    ViajeRedondo = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-contro",
            "placeholder": "Viaje"
        })
    )

    TotalCostos = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Total Costos",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly" 
        })
    )

    FactorAjustePor = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "%",
            "onkeydown" : "return numerosDecimales100(this, event);",
        })
    )

    FactorAjuste = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Factor Ajuste",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly"
        })
    )

    MopPor = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "%",
            "onkeydown" : "return numerosDecimales100(this, event);",
        })
    )

    Mop = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Mop",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly"
        })
    )

    TotalTransportista = forms.DecimalField(
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Total Transportista",
            "onkeydown" : "return numerosDecimales(this, event);",
            "readonly" : "readonly" 
        })
    )
    class Meta:
        model = Costeo
        fields = ( 'Casetas', 'Empresa', 'CPDestino', 'CPOrigen', 'Kilometros', 'ViajeRedondo', 'Producto', 'TotalCostos', 'FactorAjustePor','FactorAjuste', 'Mop', 'MopPor', 'TotalTransportista')
    