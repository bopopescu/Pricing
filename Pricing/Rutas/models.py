from django.db import models
from users import models as Users_models
"""from transportista import models as Carrier_models"""


class Rutas(models.Model):
    """IDCarrier=models.ForeignKey(Carrier_models.Transportista, on_delete=models.CASCADE, related_name='RutaAlta')"""
    CPOrigen = models.IntegerField()
    CiudadOrigen = models.CharField(max_length=254)
    EstadoOrigen = models.CharField(max_length=254)
    CPDestino = models.IntegerField(null=True, blank=True)
    CiudadDestino = models.CharField(max_length=254)
    EstadoDestino = models.CharField(max_length=254)
    ViajeRedondo = models.BooleanField()
    NombreRuta = models.CharField(max_length=254)
    Kilometros = models.DecimalField(max_digits=30, decimal_places=2)
    Date_joined = models.DateTimeField(auto_now_add=True)
    Date_Mod = models.DateTimeField(auto_now_add=True)
    IDUsuarioAlta = models.ForeignKey(Users_models.User, on_delete=models.CASCADE, related_name='RutaAlta')
    IDUsuarioMod = models.ForeignKey(Users_models.User, on_delete=models.CASCADE, related_name='RutaModi')
    Casetas = models.DecimalField(default=0, max_digits=30, decimal_places=2)
    Active= models.BooleanField(default=1)
    def __str__(self):
        return self.NombreRuta
