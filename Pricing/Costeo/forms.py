from django import forms
from Costeo.models import Depreciacion, FactoresPremisas, CostosOperativos, Costeo, Cotizacion

CHOICES=[('','Select')]

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
class CosteoForm(forms.ModelForm):
    IDTransportista = forms.IntegerField(
        widget=forms.Select(choices=CHOICES,attrs={
            "class": "form-control transportista",
            "placeholder": "transportista"
        })
    )
    IDRuta = forms.IntegerField(
        widget=forms.Select(choices=CHOICES,attrs={
            "class": "form-control ruta",
            "placeholder": "ruta"
        })
    )
    IDUnidad= forms.IntegerField(
        widget=forms.Select(choices=CHOICES,attrs={
            "class": "form-control Unidad",
            "placeholder": "Unidad"
        })
    )
    Kilometraje = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control",
            "placeholder" : "Kilometraje"
        })
    )
    Tipo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control tipo",
            "placeholder": "Tipo"
        })
    )
    Producto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control producto",
            "placeholder": "Producto"
        })
    )
    TotalCostos = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control totalCostos",
            "placeholder" : "Total Costos",
            "readonly":"readonly"
        })
    )
    Mop = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control mop",
            "placeholder" : "mop"
        })
    )
    MopPor = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control mopPor",
            "placeholder" : "mopPor"
        }),initial=15
    )
    TotalTransportista = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control totalTransportista",
            "placeholder" : "total Transportista",
            "readonly":"readonly"
        })
    )
    class Meta:
        model = Costeo
        fields = ('Kilometraje', 'Tipo', 'Producto', 'TotalCostos', 'Mop', 'MopPor', 'TotalTransportista',)

class CotizacionForm(forms.ModelForm):
    rutaid = forms.IntegerField(
        widget=forms.Select(choices=CHOICES,attrs={
            "class" : "form-control rutaid",
            "placeholder" : "Rutas",
        })
    )
    RangoPrecio = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control RangoPrecio",
            "placeholder" : "RangoPrecio",
        })
    )
    CpOrigen = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control CpOrigen",
            "placeholder" : "C.P. Origen",
        })
    )
    CpDestino = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control CpDestino",
            "placeholder" : "C.P. Destino",
        })
    )
    IDTipoUnidad = forms.IntegerField(
        widget=forms.Select(choices=CHOICES,attrs={
            "class": "form-control IDTipoUnidad",
            "placeholder": "Unidad"
        })
    )
    Productos = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control Productos",
            "placeholder": "Productos"
        })
    )
    Peso = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class" : "form-control Peso",
            "placeholder" : "Peso"
        })
    )
    class Meta:
        model = Cotizacion
        fields = ('CpOrigen', 'CpDestino', 'IDTipoUnidad', 'Productos', 'Peso',)

    
    