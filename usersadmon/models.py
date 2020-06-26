# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdmonUsuarios(models.Model):
    idusuario = models.AutoField(db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='NombreUsuario', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    apepaterno = models.CharField(db_column='ApePaterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apematerno = models.CharField(db_column='ApeMaterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fechacambiocontrasena = models.DateTimeField(db_column='FechaCambioContrasena', blank=True, null=True)  # Field name made lowercase.
    hasbytes = models.TextField(db_column='HasBytes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    saltbytes = models.TextField(db_column='SaltBytes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    periodo = models.IntegerField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.
    statusreg = models.CharField(db_column='StatusReg', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdmonUsuarios'
