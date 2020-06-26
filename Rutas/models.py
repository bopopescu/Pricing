from django.db import models
from users import models as Users_models

class Modelos(models.Model):
    Modelo = models.CharField(max_length=254)
    CostosUnidad = models.DecimalField(max_digits=30, decimal_places=2)
    CostosCaja = models.DecimalField(max_digits=30, decimal_places=2)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)
    class Meta:
        db_table = "Modelos"  

class Rutas(models.Model):
    NombreRuta = models.CharField(max_length=254)
    CPOrigen = models.IntegerField()
    CiudadOrigen = models.CharField(max_length=254)
    EstadoOrigen = models.CharField(max_length=254)
    CPDestino = models.IntegerField()
    CiudadDestino = models.CharField(max_length=254)
    EstadoDestino = models.CharField(max_length=254)
    Kilometros = models.DecimalField(max_digits=30, decimal_places=2)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
        db_table = "Rutas"

class CategoriasEjes(models.Model):
    Nombre = models.CharField(max_length=254)
    Valor = models.IntegerField()
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
        db_table = "CategoriasEjes"

class TiposUnidades(models.Model):
    Nombre = models.CharField(max_length=254)
    VolumenMax = models.FloatField()
    PesoMax = models.FloatField()
    Ancho = models.FloatField()
    Largo = models.FloatField()
    IDModelo = models.ManyToManyField(Modelos, related_name='ModelosXTipoUnidad')
    IDCategoriaEje = models.ForeignKey(CategoriasEjes, on_delete=models.CASCADE, null=True, blank=True)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
        db_table = "TiposUnidades"

class Tarifas(models.Model):
    IDRuta = models.ForeignKey(Rutas,on_delete=models.CASCADE, null=True, blank=True)
    Precio = models.DecimalField(default=0, max_digits=30, decimal_places=2)
    ViajeRedondo = models.BooleanField()
    IDTipoUnidad = models.ForeignKey(TiposUnidades,on_delete=models.CASCADE, null=True, blank=True)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
        db_table = "Tarifas"