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
    name_user=models.CharField('Nombre completo',max_length=150,blank=True,null=True)
    email_user=models.CharField('Correo corporativo',max_length=150,blank=True,null=True)
    dni_user=models.IntegerField('Documento de Identidad',blank=True,null=True)
    type_assignment=models.CharField(max_length=20, choices=TYPE_ASSIGNMENT, default="Por definir", blank=True,null=True,verbose_name=u'Tipo asignación')

    def __str__(self):
        return self.email_user
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
        
class AssignUsers(models.Model):
    creation_date=models.DateField(auto_now_add=True,verbose_name=u'Fecha de registro')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Encargado',blank=True,null=True)
    assignment= models.ForeignKey(UserData, on_delete=models.CASCADE, verbose_name=u'Encargado',blank=True,null=True)
    date_assignment=models.DateField(verbose_name=u'Fecha de asignación',blank=True,null=True)
    computers=models.ForeignKey(Computers, on_delete=models.CASCADE, null=True, blank=True,verbose_name=u'Equipo asignado')
    passive_devices=models.ManyToManyField(PassiveDevices, verbose_name=u'Dispositivos asignados')
    type_assignment=models.CharField(max_length=20, choices=TYPE_ASSIGNMENT, default="Por definir", blank=True,null=True,verbose_name=u'Tipo asignación')

    def __str__(self):
        return self.assignment
    
    class Meta:
        verbose_name = "Asignación Usuario"
        verbose_name_plural = "Asignación Usuarios"