# Generated by Django 2.1.12 on 2020-06-23 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasEjes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('Valor', models.IntegerField()),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'CategoriasEjes',
            },
        ),
        migrations.CreateModel(
            name='Modelos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=254)),
                ('CostosUnidad', models.DecimalField(decimal_places=2, max_digits=30)),
                ('CostosCaja', models.DecimalField(decimal_places=2, max_digits=30)),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'Modelos',
            },
        ),
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreRuta', models.CharField(max_length=254)),
                ('CPOrigen', models.IntegerField()),
                ('CiudadOrigen', models.CharField(max_length=254)),
                ('EstadoOrigen', models.CharField(max_length=254)),
                ('CPDestino', models.IntegerField()),
                ('CiudadDestino', models.CharField(max_length=254)),
                ('EstadoDestino', models.CharField(max_length=254)),
                ('Kilometros', models.DecimalField(decimal_places=2, max_digits=30)),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'Rutas',
            },
        ),
        migrations.CreateModel(
            name='Tarifas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Precio', models.DecimalField(decimal_places=2, default=0, max_digits=30)),
                ('ViajeRedondo', models.BooleanField()),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
                ('IDRuta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Rutas.Rutas')),
            ],
            options={
                'db_table': 'Tarifas',
            },
        ),
        migrations.CreateModel(
            name='TiposUnidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=254)),
                ('VolumenMax', models.FloatField()),
                ('PesoMax', models.FloatField()),
                ('Ancho', models.FloatField()),
                ('Largo', models.FloatField()),
                ('IDUsuarioAlta', models.IntegerField(blank=True, null=True)),
                ('IDUsuarioMod', models.IntegerField(blank=True, null=True)),
                ('FechaAlta', models.DateTimeField(blank=True, null=True)),
                ('FechaModificacion', models.DateTimeField(blank=True, null=True)),
                ('Actividad', models.BooleanField(default=1)),
                ('IDCategoriaEje', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Rutas.CategoriasEjes')),
                ('IDModelo', models.ManyToManyField(related_name='ModelosXTipoUnidad', to='Rutas.Modelos')),
            ],
            options={
                'db_table': 'TiposUnidades',
            },
        ),
        migrations.AddField(
            model_name='tarifas',
            name='IDTipoUnidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Rutas.TiposUnidades'),
        ),
    ]
