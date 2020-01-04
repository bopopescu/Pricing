# Generated by Django 2.1.12 on 2020-01-03 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Rutas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField()),
                ('RepLGK', models.CharField(blank=True, max_length=254, null=True)),
                ('RepTransportista', models.CharField(blank=True, max_length=254, null=True)),
                ('Active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FormatoAlta', models.FileField(upload_to='documents/')),
                ('ActaConstitutiva', models.FileField(upload_to='documents/')),
                ('CedulaFiscal', models.FileField(upload_to='documents/')),
                ('IFERepresentante', models.FileField(upload_to='documents/')),
                ('ComprobanteDomicilio', models.FileField(upload_to='documents/')),
                ('CaratulaBancaria', models.FileField(upload_to='documents/')),
                ('ConvenioConfidencialidad', models.FileField(upload_to='documents/')),
                ('ContratoServicios', models.FileField(upload_to='documents/')),
                ('ConvenioTarifas', models.FileField(upload_to='documents/')),
                ('Descripcion', models.FileField(upload_to='documents/')),
                ('Permisos', models.FileField(upload_to='documents/')),
                ('Licencias', models.FileField(upload_to='documents/')),
                ('Active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(upload_to='documents/')),
                ('Stars', models.IntegerField(default=0)),
                ('TarjetaDirector', models.FileField(upload_to='documents/')),
                ('TarjetaVentas', models.FileField(upload_to='documents/')),
                ('Active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Remolque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('Marca', models.CharField(max_length=254)),
                ('Modelo', models.CharField(max_length=254)),
                ('Anno', models.IntegerField(default=0)),
                ('Placas', models.CharField(max_length=30, unique=True)),
                ('Econnum', models.CharField(max_length=254)),
                ('NumeroSatelital', models.IntegerField(default=0)),
                ('Volumen', models.IntegerField(default=0)),
                ('Peso', models.IntegerField(default=0)),
                ('Longitud', models.IntegerField(default=0)),
                ('Ancho', models.IntegerField(default=0)),
                ('PlacasTraseras', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('Seguro', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('FacturaRemolque', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('Active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tarifas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipo', models.CharField(max_length=254)),
                ('Origen', models.CharField(max_length=254)),
                ('Destino', models.CharField(max_length=254)),
                ('Tarifa', models.DecimalField(decimal_places=2, max_digits=30)),
                ('Moneda', models.CharField(max_length=254)),
                ('Comentarios', models.TextField()),
                ('Evidencia', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('Active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RazonSocial', models.CharField(max_length=254)),
                ('Email', models.EmailField(max_length=254)),
                ('NombreComercial', models.CharField(max_length=254)),
                ('Calle', models.CharField(blank=True, max_length=254, null=True)),
                ('NumInt', models.CharField(blank=True, max_length=254, null=True)),
                ('NumExt', models.CharField(blank=True, max_length=254, null=True)),
                ('Estado', models.CharField(blank=True, max_length=254, null=True)),
                ('Ciudad', models.CharField(blank=True, max_length=254, null=True)),
                ('CP', models.IntegerField(blank=True, null=True)),
                ('Colonia', models.CharField(blank=True, max_length=254, null=True)),
                ('BaseTerminal', models.CharField(blank=True, max_length=254, null=True)),
                ('Telefonos', models.CharField(blank=True, max_length=254, null=True)),
                ('PaginaWeb', models.CharField(blank=True, max_length=254, null=True)),
                ('Actividad', models.CharField(blank=True, max_length=254, null=True)),
                ('Credito', models.IntegerField(blank=True, null=True)),
                ('Is_active', models.IntegerField(default=1)),
                ('Date_joined', models.DateTimeField(auto_now_add=True)),
                ('Date_Mod', models.DateTimeField(auto_now_add=True)),
                ('NombreContacto', models.CharField(max_length=254)),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('Active', models.BooleanField(default=1)),
                ('IDRutas', models.ManyToManyField(related_name='RutasXCarrier', to='Rutas.Rutas')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('Combustible', models.CharField(max_length=254)),
                ('Performance', models.IntegerField(default=0)),
                ('RegistroVehiculo', models.IntegerField(default=0)),
                ('RegistroTarjeta', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('FechaExpiracion', models.DateTimeField()),
                ('Marca', models.CharField(max_length=254)),
                ('Modelo', models.CharField(max_length=254)),
                ('Anno', models.IntegerField(default=0)),
                ('Placas', models.CharField(max_length=30, unique=True)),
                ('Econnum', models.CharField(max_length=254, unique=True)),
                ('NumeroSatelital', models.IntegerField(default=0)),
                ('PlacasTraseras', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('Seguro', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('Special', models.BooleanField()),
                ('FullUnit', models.BooleanField()),
                ('Active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('Capacidad', models.IntegerField(default=0)),
                ('Medidas', models.CharField(blank=True, max_length=30, null=True)),
                ('Configuraciones', models.CharField(blank=True, max_length=254, null=True)),
                ('Image', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('Active', models.BooleanField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='unidad',
            name='IDTipoUnidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transportista.UnidadType'),
        ),
        migrations.AddField(
            model_name='unidad',
            name='IDTransportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transportista.Transportista'),
        ),
        migrations.AddField(
            model_name='remolque',
            name='IDTipoUnidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transportista.UnidadType'),
        ),
        migrations.AddField(
            model_name='remolque',
            name='IDTransportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transportista.Transportista'),
        ),
        migrations.AddField(
            model_name='extras',
            name='IDTransportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transportista.Transportista'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='IDTransportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transportista.Transportista'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='IDTransportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transportista.Transportista'),
        ),
    ]
