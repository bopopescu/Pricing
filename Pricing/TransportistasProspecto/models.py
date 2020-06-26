from django.db import models
from users import models as Users_models
from Rutas.models import Tarifas, TiposUnidades

class Contactos(models.Model):
    Profesion = models.CharField(max_length=254, null=True, blank=True)
    NombreIFE = models.CharField(max_length=254)
    PrimerNombre = models.CharField(max_length=254)
    SegundoNombre = models.CharField(max_length=254, null=True, blank=True)
    ApellidoPaterno = models.CharField(max_length=254)
    ApellidoMaterno = models.CharField(max_length=254)
    Puesto  = models.CharField(max_length=254, null=True, blank=True)
    Telefono = models.CharField(max_length=254)
    Correo= models.CharField(max_length=254)
    CorreoAdicional = models.CharField(max_length=254, null=True, blank=True)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)
    class Meta:
        db_table = "Contactos"

class Certificaciones(models.Model):
    Nombre = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
            db_table = "Certificaciones"

class Prioridades(models.Model):
    Nombre = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
            db_table = "Prioridades"

class Estatus(models.Model):
    Nombre = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
            db_table = "Estatus"

class Tipos(models.Model):
    Nombre = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
            db_table = "Tipos"

class TransportistasProspectos(models.Model):
    RazonSocial = models.CharField(max_length=254)
    NombreComercial = models.CharField(max_length=254)
    RFC = models.CharField(max_length=254)
    PaginaWeb = models.CharField(max_length=254)
    Municipio = models.CharField(max_length=254)
    Estado = models.CharField(max_length=254)
    Pais = models.CharField(max_length=254)
    CodigoPostal = models.IntegerField()
    Calle = models.CharField(max_length=254)
    NumeroExt = models.CharField(max_length=254, null=True, blank=True)
    NumeroInt = models.CharField(max_length=254, null=True, blank=True)
    Colonia = models.CharField(max_length=254)
    Seguridad = models.CharField(max_length=254, null=True, blank=True)
    PolizaSeguro = models.CharField(max_length=254, null=True, blank=True)
    Credito = models.IntegerField(null=True, blank=True)
    IDPrioridad = models.ForeignKey(Prioridades, on_delete=models.CASCADE, null=True, blank=True)
    IDEstatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, null=True, blank=True)
    IDTipo = models.ManyToManyField(Tipos, related_name='TiposXTransportita')
    IDTipoUnidad = models.ManyToManyField(TiposUnidades, related_name='TiposUnidadesXTransportita')
    IDCertificacion = models.ManyToManyField(Certificaciones, related_name='CertificacionesXTransportita')
    IDTarifa = models.ManyToManyField(Tarifas, related_name='TarifasXTransportita')
    IDContacto = models.ManyToManyField(Contactos, related_name='ContactosXTransportistas')
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
        db_table = "TransportistasProspectos"




"""
from django.db import models
from users import models as Users_models
from Rutas.models import Tarifas, TiposUnidades

class Contactos(models.Model):
    #Profesion = models.CharField(max_length=254)
    Profesion = models.CharField(max_length=254, null=True, blank=True)
    NombreIFE = models.CharField(max_length=254)
    PrimerNombre = models.CharField(max_length=254)
    SegundoNombre = models.CharField(max_length=254, null=True, blank=True)
    #SegundoNombre = models.CharField(max_length=254)
    ApellidoPaterno = models.CharField(max_length=254)
    ApellidoMaterno = models.CharField(max_length=254)
    Puesto  = models.CharField(max_length=254, null=True, blank=True)
    #Puesto  = models.CharField(max_length=254)
    Telefono = models.CharField(max_length=254)
    Correo= models.CharField(max_length=254)
    CorreoAdicional = models.CharField(max_length=254, null=True, blank=True)
    #CorreoAdicional = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)
    class Meta:
        db_table = "Contactos"

class Certificaciones(models.Model):
    Nombre = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
            db_table = "Certificaciones"

class Prioridades(models.Model):
    Nombre = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
            db_table = "Prioridades"

class Estatus(models.Model):
    Nombre = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
            db_table = "Estatus"

class Tipos(models.Model):
    Nombre = models.CharField(max_length=254)
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
            db_table = "Tipos"

class TransportistasProspectos(models.Model):
    RazonSocial = models.CharField(max_length=254)
    NombreComercial = models.CharField(max_length=254)
    RFC = models.CharField(max_length=254)
    PaginaWeb = models.CharField(max_length=254, null=True, blank=True)
    #PaginaWeb = models.CharField(max_length=254)
    Municipio = models.CharField(max_length=254)
    Estado = models.CharField(max_length=254)
    Pais = models.CharField(max_length=254)
    CodigoPostal = models.IntegerField()
    Calle = models.CharField(max_length=254)
    NumeroExt = models.CharField(max_length=254, null=True, blank=True)
    #NumeroExt = models.CharField(max_length=254)
    NumeroInt = models.CharField(max_length=254, null=True, blank=True)
    #NumeroInt = models.CharField(max_length=254)
    Colonia = models.CharField(max_length=254)
    Seguridad = models.CharField(max_length=254, null=True, blank=True)
    #Seguridad = models.CharField(max_length=254)
    PolizaSeguro = models.CharField(max_length=254, null=True, blank=True)
    Credito = models.IntegerField(null=True, blank=True)
    #Credito = models.IntegerField()
    IDPrioridad = models.ForeignKey(Prioridades, on_delete=models.CASCADE, null=True, blank=True)
    IDEstatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, null=True, blank=True)
    IDTipo = models.ForeignKey(Tipos, on_delete=models.CASCADE,  null=True, blank=True)
    IDTipoUnidad = models.ManyToManyField(TiposUnidades, related_name='TiposUnidadesXTransportita')
    IDCertificacion = models.ManyToManyField(Certificaciones, related_name='CertificacionesXTransportita')
    IDTarifa = models.ManyToManyField(Tarifas, related_name='TarifasXTransportita')
    IDContacto = models.ManyToManyField(Contactos, related_name='ContactosXTransportistas')
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    FechaAlta = models.DateTimeField(null=True, blank=True)
    FechaModificacion = models.DateTimeField(null=True, blank=True)
    Actividad= models.BooleanField(default=1)

    class Meta:
        db_table = "TransportistasProspectos"
"""