# Generated by Django 2.1.12 on 2020-06-23 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Rutas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'Certificaciones',
            },
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profesion', models.CharField(max_length=254)),
                ('NombreIFE', models.CharField(max_length=254)),
                ('PrimerNombre', models.CharField(max_length=254)),
                ('SegundoNombre', models.CharField(max_length=254)),
                ('ApellidoPaterno', models.CharField(max_length=254)),
                ('ApellidoMaterno', models.CharField(max_length=254)),
                ('Puesto', models.CharField(max_length=254)),
                ('Telefono', models.CharField(max_length=254)),
                ('Correo', models.CharField(max_length=254)),
                ('CorreoAdicional', models.CharField(max_length=254)),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'Estatus',
            },
        ),
        migrations.CreateModel(
            name='Prioridades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'Prioridades',
            },
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='TransportistasProspectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RazonSocial', models.CharField(max_length=254)),
                ('NombreComercial', models.CharField(max_length=254)),
                ('RFC', models.CharField(max_length=254)),
                ('PaginaWeb', models.CharField(max_length=254)),
                ('Municipio', models.CharField(max_length=254)),
                ('Estado', models.CharField(max_length=254)),
                ('Pais', models.CharField(max_length=254)),
                ('CodigoPostal', models.IntegerField()),
                ('Calle', models.CharField(max_length=254)),
                ('NumeroExt', models.CharField(max_length=254)),
                ('NumeroInt', models.CharField(max_length=254)),
                ('Colonia', models.CharField(max_length=254)),
                ('Seguridad', models.CharField(blank=True, max_length=254)),
                ('PolizaSeguro', models.CharField(max_length=254)),
                ('Credito', models.IntegerField()),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
                ('IDCertificacion', models.ManyToManyField(related_name='CertificacionesXTransportita', to='TransportistasProspecto.Certificaciones')),
                ('IDContacto', models.ManyToManyField(related_name='ContactosXTransportistas', to='TransportistasProspecto.Contactos')),
                ('IDEstatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TransportistasProspecto.Estatus')),
                ('IDPrioridad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TransportistasProspecto.Prioridades')),
                ('IDTarifa', models.ManyToManyField(related_name='TarifasXTransportita', to='Rutas.Tarifas')),
                ('IDTipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TransportistasProspecto.Tipos')),
                ('IDTipoUnidad', models.ManyToManyField(related_name='TiposUnidadesXTransportita', to='Rutas.TiposUnidades')),
            ],
            options={
                'db_table': 'TransportistasProspectos',
            },
        ),
    ]
