from django.db import models
from users import models as Users_models
from Transportista import models as carrier_models


class EquipoDisponible(models.Model):
    IDEquipodisponible = models.AutoField(primary_key=True)
    Carrier = models.ForeignKey(carrier_models.Transportista, on_delete=models.CASCADE,
                                related_name='CarrierDisponible',blank=True)
    rutas = models.ForeignKey(carrier_models.rutas_models.Rutas, on_delete=models.CASCADE,
                              related_name='EquipoDisponible',blank=True)
    Disponibles = models.IntegerField(blank=True)
    Ocupado = models.IntegerField(blank=True)
    NoUnidades = models.IntegerField(null=True, blank=True)

    def _str_(self):
    	return self.Disponibles
