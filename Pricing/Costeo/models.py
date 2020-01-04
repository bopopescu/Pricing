from django.db import models
from Transportista import models as carrier_models


class Depreciacion(models.Model):
    Meses = models.IntegerField()
    CostosUnidad = models.DecimalField(max_digits=30, decimal_places=2)
    CostosCaja = models.DecimalField(max_digits=30, decimal_places=2)
    ViajesMes = models.IntegerField()
    KmsMesXunidad = models.DecimalField(max_digits=30, decimal_places=2)
    KmsMaximo = models.DecimalField(max_digits=30, decimal_places=2)
    DepTracto = models.DecimalField(max_digits=30, decimal_places=2)
    DepCaja = models.DecimalField(max_digits=30, decimal_places=2)
    RentaGPS = models.DecimalField(max_digits=30, decimal_places=2)
    PlacasTenencia = models.DecimalField(max_digits=30, decimal_places=2)
    Seguro = models.DecimalField(max_digits=30, decimal_places=2)
    Admvo = models.IntegerField()
    Financieros = models.IntegerField()
    MttoUnidadXkm = models.DecimalField(max_digits=30, decimal_places=2)
    Llantas = models.DecimalField(max_digits=30, decimal_places=2)
    Operador = models.DecimalField(max_digits=30, decimal_places=2)
    DobleOp = models.DecimalField(max_digits=30, decimal_places=2)


class FactoresPremisas(models.Model):
    Unidad = models.IntegerField()
    Caja = models.IntegerField()
    KmSencillo = models.DecimalField(max_digits=30, decimal_places=2)
    KmRoundTrip = models.DecimalField(max_digits=30, decimal_places=2)
    KmMensuales = models.DecimalField(max_digits=30, decimal_places=2)
    CasetaSingle = models.DecimalField(max_digits=30, decimal_places=2)
    Rendimiento = models.DecimalField(max_digits=30, decimal_places=2)
    Diesel = models.DecimalField(max_digits=30, decimal_places=2)
    DieselSinIva = models.DecimalField(max_digits=30, decimal_places=2)


class CostosOperativos(models.Model):
    """Directo Varieble"""
    Combustible = models.DecimalField(max_digits=30, decimal_places=2)
    Casetas = models.DecimalField(max_digits=30, decimal_places=2)
    Operador = models.DecimalField(max_digits=30, decimal_places=2)
    Subtotal1 = models.DecimalField(max_digits=30, decimal_places=2)
    """Indirecto fijo"""
    MttoUnidad = models.DecimalField(max_digits=30, decimal_places=2)
    LlantasUnidad = models.DecimalField(max_digits=30, decimal_places=2)
    Gps = models.DecimalField(max_digits=30, decimal_places=2)
    Seguro = models.DecimalField(max_digits=30, decimal_places=2)
    PlacasTenencia = models.DecimalField(max_digits=30, decimal_places=2)
    SubTotal2 = models.DecimalField(max_digits=30, decimal_places=2)
    """Admvo & Financiero"""
    Admvo = models.DecimalField(max_digits=30, decimal_places=2)
    Financieros = models.DecimalField(max_digits=30, decimal_places=2)
    DeprUnidad = models.DecimalField(max_digits=30, decimal_places=2)
    DeprRemolque = models.DecimalField(max_digits=30, decimal_places=2)
    Subtotal3 = models.DecimalField(max_digits=30, decimal_places=2)


class Costeo(models.Model):
    IDTransportista = models.ForeignKey(carrier_models.Transportista, on_delete=models.CASCADE, blank=True, null=True)
    IDRuta = models.ForeignKey(carrier_models.rutas_models.Rutas, on_delete=models.CASCADE)
    IDDepreciacion = models.ForeignKey(Depreciacion, on_delete=models.CASCADE)
    IDFactoresPremisas = models.ForeignKey(FactoresPremisas, on_delete=models.CASCADE)
    IDCostosOperativos = models.ForeignKey(CostosOperativos, on_delete=models.CASCADE)
    IDUnidad = models.ForeignKey(carrier_models.Unidad, on_delete=models.CASCADE, blank=True, null=True)
    Kilometraje = models.DecimalField(max_digits=30, decimal_places=2)
    Tipo = models.CharField(max_length=254)
    Producto = models.CharField(max_length=254)
    TotalCostos = models.DecimalField(max_digits=30, decimal_places=2)
    Mop = models.DecimalField(max_digits=30, decimal_places=2)
    MopPor = models.DecimalField(max_digits=30, decimal_places=2)
    TotalTransportista = models.DecimalField(max_digits=30, decimal_places=2)
    Descripcion = models.TextField()
    Active= models.BooleanField(default=1)


class Cotizacion(models.Model):
    rutaid = models.IntegerField()
    CpOrigen = models.IntegerField()
    CpDestino = models.IntegerField()
    IDTipoUnidad = models.ForeignKey(carrier_models.UnidadType, on_delete=models.CASCADE, blank=True,
                                     null=True)
    Productos = models.CharField(max_length=254)
    Peso = models.DecimalField(max_digits=30, decimal_places=2)
    IDCosteo = models.ForeignKey(Costeo, on_delete=models.CASCADE)
    RangoPrecio = models.DecimalField(max_digits=30, decimal_places=2)