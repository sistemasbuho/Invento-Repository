# Generated by Django 4.1 on 2023-01-20 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actives', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('name_user', models.CharField(max_length=150, verbose_name='Nombre completo')),
                ('email_user', models.CharField(max_length=150, unique=True, verbose_name='Correo corporativo')),
                ('dni_user', models.IntegerField(unique=True, verbose_name='Documento de Identidad')),
                ('type_assignment', models.CharField(choices=[('Contrato fijo', 'Contrato fijo'), ('Contrato indefinido', 'Contrato indefinido'), ('Prestamo', 'Prestamo'), ('Fijo al area', 'Fijo al area'), ('Aprendiz', 'Aprendiz'), ('Practicante', 'Practicante'), ('Contrato prestacion', 'Contrato prestacion'), ('Por definir', 'Por definir')], default='Por definir', max_length=20, verbose_name='Tipo asignación')),
                ('digital_sign', models.ImageField(blank=True, null=True, upload_to='assign_user', verbose_name='Firma Digital')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='AssignUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('date_assignment', models.DateField(verbose_name='Fecha de asignación')),
                ('image_up_pc', models.ImageField(blank=True, null=True, upload_to='assign_user', verbose_name='Imagen Equipo superior')),
                ('image_front_pc', models.ImageField(blank=True, null=True, upload_to='assign_user', verbose_name='Imagen Equipo frontal')),
                ('image_back_pc', models.ImageField(blank=True, null=True, upload_to='assign_user', verbose_name='Imagen Equipo debajo')),
                ('image_monitor', models.ImageField(blank=True, null=True, upload_to='assign_user', verbose_name='Imagen monitor')),
                ('image_keyboard', models.ImageField(blank=True, null=True, upload_to='assign_user', verbose_name='Imagen teclado')),
                ('image_devices', models.ImageField(blank=True, null=True, upload_to='assign_user', verbose_name='Imagen dispositivos')),
                ('image_others', models.ImageField(blank=True, null=True, upload_to='assign_user', verbose_name='Imagen Otros elementos')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.userdata', verbose_name='Encargado')),
                ('computers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actives.computers', verbose_name='Equipo asignado')),
                ('monitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='actives.monitors', verbose_name='Monitor asignado')),
                ('passive_devices', models.ManyToManyField(to='actives.passivedevices', verbose_name='Dispositivos asignados')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Encargado')),
            ],
            options={
                'verbose_name': 'Asignación Usuario',
                'verbose_name_plural': 'Asignación Usuarios',
            },
        ),
    ]
