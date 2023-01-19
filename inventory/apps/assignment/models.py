from django.db import models
from django.contrib.auth.models import User
from apps.actives.models import Computers, PassiveDevices

TYPE_ASSIGNMENT=(
	("Contrato fijo","Contrato fijo"),
    ("Contrato indefinido","Contrato indefinido"),
	("Prestamo","Prestamo"),
	("Fijo al area","Fijo al area"),
    ("Aprendiz","Aprendiz"),
    ("Practicante","Practicante"),
    ("Contrato prestacion","Contrato prestacion"),
	("Por definir","Por definir"),)

class UserData(models.Model):
    creation_date=models.DateField(auto_now_add=True,verbose_name=u'Fecha de registro')
    name_user=models.CharField('Nombre completo',max_length=150)
    email_user=models.CharField('Correo corporativo',max_length=150)
    dni_user=models.IntegerField('Documento de Identidad')
    type_assignment=models.CharField(max_length=20, choices=TYPE_ASSIGNMENT, default="Por definir",verbose_name=u'Tipo asignación')

    def __str__(self):
        return self.email_user
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
        
class AssignUsers(models.Model):
    creation_date=models.DateField(auto_now_add=True,verbose_name=u'Fecha de registro')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Encargado')
    assignment= models.ForeignKey(UserData, on_delete=models.CASCADE, verbose_name=u'Encargado')
    date_assignment=models.DateField(verbose_name=u'Fecha de asignación')
    computers=models.ForeignKey(Computers, on_delete=models.CASCADE, verbose_name=u'Equipo asignado')
    passive_devices=models.ManyToManyField(PassiveDevices, verbose_name=u'Dispositivos asignados')
    type_assignment=models.CharField(max_length=20, choices=TYPE_ASSIGNMENT, default="Por definir",verbose_name=u'Tipo asignación')

    
    class Meta:
        verbose_name = "Asignación Usuario"
        verbose_name_plural = "Asignación Usuarios"