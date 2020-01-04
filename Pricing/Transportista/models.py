from django.db import models
from users import models as Users_models
from Rutas import models as rutas_models
import os


class Transportista(models.Model):
    RazonSocial = models.CharField(max_length=254)
    Email = models.EmailField(max_length=254)
    NombreComercial = models.CharField(max_length=254)
    Calle = models.CharField(max_length=254, null=True, blank=True)
    NumInt = models.CharField(max_length=254, null=True, blank=True)
    NumExt = models.CharField(max_length=254, null=True, blank=True)
    Estado = models.CharField(max_length=254, null=True, blank=True)
    Ciudad = models.CharField(max_length=254, null=True, blank=True)
    CP = models.IntegerField(null=True, blank=True)
    Colonia = models.CharField(max_length=254, null=True, blank=True)
    BaseTerminal = models.CharField(max_length=254, null=True, blank=True)
    Telefonos = models.CharField(max_length=254, null=True, blank=True)
    PaginaWeb = models.CharField(max_length=254, null=True, blank=True)
    Actividad = models.CharField(max_length=254, null=True, blank=True)
    Credito = models.IntegerField(null=True, blank=True)
    Is_active = models.IntegerField(default=1)
    Date_joined = models.DateTimeField(auto_now_add=True)
    Date_Mod = models.DateTimeField(auto_now_add=True)
    NombreContacto = models.CharField(max_length=254)
    IDRutas = models.ManyToManyField(rutas_models.Rutas, related_name='RutasXCarrier')
    IDUsuarioAlta = models.IntegerField(null=True, blank=True)
    IDUsuarioMod = models.IntegerField(null=True, blank=True)
    Active=models.BooleanField(default=1)

    def __str__(self):
        return self.RazonSocial


class Expediente(models.Model):
    IDTransportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
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


class Extras(models.Model):
    IDTransportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    Image = models.FileField(upload_to='documents/')
    Stars = models.IntegerField(default=0)
    TarjetaDirector = models.FileField(upload_to='documents/')
    TarjetaVentas = models.FileField(upload_to='documents/')
    Active=models.BooleanField(default=1)


class Bitacora(models.Model):
    IDTransportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    Fecha = models.DateTimeField()
    RepLGK = models.CharField(max_length=254, null=True, blank=True)
    RepTransportista = models.CharField(max_length=254, null=True, blank=True)
    Active=models.BooleanField(default=1)


class UnidadType(models.Model):
    Nombre = models.CharField(max_length=254)
    Capacidad = models.IntegerField(default=0)
    Medidas = models.CharField(max_length=30, null=True, blank=True)
    Configuraciones = models.CharField(max_length=254, null=True, blank=True)
    Image = models.FileField(upload_to='documents/', null=True, blank=True)
    Active=models.BooleanField(default=1)

    def __str__(self):
        return self.Nombre


class Unidad(models.Model):
    IDTransportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    IDTipoUnidad = models.ForeignKey(UnidadType, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=254)
    Combustible = models.CharField(max_length=254)
    Performance = models.IntegerField(default=0)
    RegistroVehiculo = models.IntegerField(default=0)
    RegistroTarjeta = models.FileField(upload_to='documents/', null=True, blank=True)
    FechaExpiracion = models.DateTimeField()
    Marca = models.CharField(max_length=254)
    Modelo = models.CharField(max_length=254)
    Anno = models.IntegerField(default=0)
    Placas = models.CharField(max_length=30, unique=True)
    Econnum = models.CharField(max_length=254, unique=True)
    NumeroSatelital = models.IntegerField(default=0)
    PlacasTraseras = models.FileField(upload_to='documents/', null=True, blank=True)
    Seguro = models.FileField(upload_to='documents/', null=True, blank=True)
    Special = models.BooleanField()
    FullUnit = models.BooleanField()
    Active=models.BooleanField(default=1)

    def __str__(self):
        return self.Nombre


class Tarifas(models.Model):
    Equipo = models.CharField(max_length=254)
    Origen = models.CharField(max_length=254)
    Destino = models.CharField(max_length=254)
    Tarifa = models.DecimalField(max_digits=30, decimal_places=2)
    Moneda = models.CharField(max_length=254)
    Comentarios = models.TextField()
    Evidencia = models.FileField(upload_to='documents/', null=True, blank=True)
    Active=models.BooleanField(default=1)


class Remolque(models.Model):
    IDTransportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    IDTipoUnidad = models.ForeignKey(UnidadType, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=254)
    Marca = models.CharField(max_length=254)
    Modelo = models.CharField(max_length=254)
    Anno = models.IntegerField(default=0)
    Placas = models.CharField(max_length=30, unique=True)
    Econnum = models.CharField(max_length=254)
    NumeroSatelital = models.IntegerField(default=0)
    Volumen = models.IntegerField(default=0)
    Peso = models.IntegerField(default=0)
    Longitud = models.IntegerField(default=0)
    Ancho = models.IntegerField(default=0)
    PlacasTraseras = models.FileField(upload_to='documents/', null=True, blank=True)
    Seguro = models.FileField(upload_to='documents/', null=True, blank=True)
    FacturaRemolque = models.FileField(upload_to='documents/', null=True, blank=True)
    Active=models.BooleanField(default=1)
