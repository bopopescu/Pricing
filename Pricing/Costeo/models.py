from django.db import models
from TransportistasProspecto.models import TransportistasProspectos
from Rutas.models import Rutas, TiposUnidades, Modelos

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
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)
    class Meta:
        db_table = "Depreciacion"

class FactoresPremisas(models.Model):
    Unidad = models.IntegerField()
    Caja = models.IntegerField()
    Km = models.DecimalField(max_digits=30, decimal_places=2)
    KmMensuales = models.DecimalField(max_digits=30, decimal_places=2)
    CasetaSingle = models.DecimalField(max_digits=30, decimal_places=2)
    Rendimiento = models.DecimalField(max_digits=30, decimal_places=2)
    Diesel = models.DecimalField(max_digits=30, decimal_places=2)
    DieselSinIva = models.DecimalField(max_digits=30, decimal_places=2)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)
    class Meta:
        db_table = "FactoresPremisas"

class CostosOperativos(models.Model):
    #Directo Varieble
    Combustible = models.DecimalField(max_digits=30, decimal_places=2)
    Casetas = models.DecimalField(max_digits=30, decimal_places=2)
    Operador = models.DecimalField(max_digits=30, decimal_places=2)
    Subtotal1 = models.DecimalField(max_digits=30, decimal_places=2)
    #Indirecto fijo
    MttoUnidad = models.DecimalField(max_digits=30, decimal_places=2)
    LlantasUnidad = models.DecimalField(max_digits=30, decimal_places=2)
    Gps = models.DecimalField(max_digits=30, decimal_places=2)
    Seguro = models.DecimalField(max_digits=30, decimal_places=2)
    PlacasTenencia = models.DecimalField(max_digits=30, decimal_places=2)
    SubTotal2 = models.DecimalField(max_digits=30, decimal_places=2)
    #Admvo & Financiero
    Admvo = models.DecimalField(max_digits=30, decimal_places=2)
    Financieros = models.DecimalField(max_digits=30, decimal_places=2)
    DeprUnidad = models.DecimalField(max_digits=30, decimal_places=2)
    DeprRemolque = models.DecimalField(max_digits=30, decimal_places=2)
    Subtotal3 = models.DecimalField(max_digits=30, decimal_places=2)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)
    class Meta:
        db_table = "CostosOperativos"

class Costeo(models.Model):
    IDRuta = models.ForeignKey(Rutas, on_delete=models.CASCADE)
    CPOrigen = models.CharField(max_length=254)
    CPDestino = models.CharField(max_length=254)
    Empresa = models.CharField(max_length=254)
    Casetas =  models.DecimalField(max_digits=30, decimal_places=2)
    IDDepreciacion = models.ForeignKey(Depreciacion, on_delete=models.CASCADE)
    IDFactoresPremisas = models.ForeignKey(FactoresPremisas, on_delete=models.CASCADE)
    IDCostosOperativos = models.ForeignKey(CostosOperativos, on_delete=models.CASCADE)
    IDTipoUnidad =  models.ForeignKey(TiposUnidades, on_delete=models.CASCADE, null=True, blank=True)
    IDModelo =  models.ForeignKey(Modelos, on_delete=models.CASCADE, null=True, blank=True)
    Kilometros = models.DecimalField(max_digits=30, decimal_places=2)
    Producto = models.CharField(max_length=254)
    TotalCostos = models.DecimalField(max_digits=30, decimal_places=2)
    FactorAjustePor = models.DecimalField(max_digits=30, decimal_places=2)
    FactorAjuste = models.DecimalField(max_digits=30, decimal_places=2)
    Mop = models.DecimalField(max_digits=30, decimal_places=2)
    MopPor = models.DecimalField(max_digits=30, decimal_places=2)
    TotalTransportista = models.DecimalField(max_digits=30, decimal_places=2)
    ViajeRedondo = models.BooleanField()
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)
    class Meta:
        db_table = "Costeo"   