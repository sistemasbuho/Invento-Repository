from django.db import models
from django.contrib.auth.models import User
from apps.actives.models import Computers, PassiveDevices


class AssignUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Asignación')
    date_assignment=models.DateField(verbose_name=u'Fecha de asignación',blank=True,null=True)
    computers=models.ForeignKey(Computers, on_delete=models.CASCADE, null=True, blank=True,verbose_name=u'Equipo asignado')
    passive_devices=models.ManyToManyField(PassiveDevices, verbose_name=u'Dispositivos asignados')
