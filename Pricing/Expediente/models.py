from django.db import models
import os
class Expediente(models.Model):
    IDTransportista = models.IntegerField(default=0)
    FormatoAlta = models.FileField(upload_to='documents/')
    ActaConstitutiva = models.FileField(upload_to='documents/')
    CedulaFiscal = models.FileField(upload_to='documents/')
    IFERepresentante = models.FileField(upload_to='documents/')
    ComprobanteDomicilio = models.FileField(upload_to='documents/')
    CaratulaBancaria = models.FileField(upload_to='documents/')
    ConvenioConfidencialidad = models.FileField(upload_to='documents/')
    ContratoServicios = models.FileField(upload_to='documents/')
    ConvenioTarifas = models.FileField(upload_to='documents/')
    Descripcion = models.FileField(upload_to='documents/')
    Permisos = models.FileField(upload_to='documents/')
    Licencias = models.FileField(upload_to='documents/')
    Active=models.BooleanField(default=1)

    def extensionActCon(self):
        name, extension = os.path.splitext(self.ActaConstitutiva.name)
        return extension

    def extensionFormAlt(self):
        name, extension = os.path.splitext(self.FormatoAlta.name)
        return extension

    def extensionCedFis(self):
        name, extension = os.path.splitext(self.CedulaFiscal.name)
        return extension

    def extensionIFE(self):
        name, extension = os.path.splitext(self.IFERepresentante.name)
        return extension

    def extensionComDom(self):
        name, extension = os.path.splitext(self.ComprobanteDomicilio.name)
        return extension

    def extensionCarBan(self):
        name, extension = os.path.splitext(self.CaratulaBancaria.name)
        return extension

    def extensionConCon(self):
        name, extension = os.path.splitext(self.ConvenioConfidencialidad.name)
        return extension

    def extensionConSer(self):
        name, extension = os.path.splitext(self.ContratoServicios.name)
        return extension

    def extensionConTar(self):
        name, extension = os.path.splitext(self.ConvenioTarifas.name)
        return extension

    def extensionDes(self):
        name, extension = os.path.splitext(self.Descripcion.name)
        return extension

    def extensionPer(self):
        name, extension = os.path.splitext(self.Permisos.name)
        return extension

    def extensionLic(self):
        name, extension = os.path.splitext(self.Licencias.name)
        return extension

    class Meta:
        db_table = "Expediente"

class Extras(models.Model):
    IDTransportista = models.IntegerField(default=0)
    Image = models.FileField(upload_to='documents/')
    Stars = models.IntegerField(default=0)
    TarjetaDirector = models.FileField(upload_to='documents/')
    TarjetaVentas = models.FileField(upload_to='documents/')
    Active=models.BooleanField(default=1)

    class Meta:
        db_table = "Extras"

"""
Borrar
"""
class Bitacora(models.Model):
    IDTransportista = models.IntegerField(default=0)
    Fecha = models.DateTimeField()
    RepLGK = models.CharField(max_length=254, null=True, blank=True)
    RepTransportista = models.CharField(max_length=254, null=True, blank=True)
    Active=models.BooleanField(default=1)

    class Meta:
        db_table = "Bitacora"