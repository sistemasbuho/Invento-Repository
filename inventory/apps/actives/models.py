from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe


STATES=(
	("Activo asignado","Activo asignado"),
    ("Activo disponible","Activo disponible"),
	("Mantenimiento","Mantenimiento"),
	("Dado de baja","Dado de baja"),
	("Por definir","Por definir"),)

TYPE_MANUFACTURER=(
	("Para equipos","Para equipos"),
 	("Para monitor","Para monitor"),
    ("Para dispositivos","Para dispositivos"),
    ("Todos","Todos"),
)


TYPE_MAINTENANCE=(
	("Correctivo","Correctivo"),
    ("Preventivo","Preventivo"),
)


STATE_PROCESS=(
	("Pendiente","Pendiente"),
    ("En curso","En curso"),
    ("Finalizado","Finalizado"),
)

PRIORITY=(
	("Alta","Alta"),
    ("Media","Media"),
    ("Baja","Baja"),
    ("Por definir","Por definir"),
)

class TypeDevices(models.Model):
    name=models.CharField('Nombre',max_length=150)

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = "Dispositivos"
        verbose_name_plural = "Dispositivos"
        
        
class Manufacturer(models.Model):
    name=models.CharField('Nombre',max_length=150,unique=True)

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"
     

class ModelManufacturer(models.Model):
    model=models.CharField('Nombre',max_length=150,unique=True)
    product_image=models.ImageField(upload_to="product_image",null=True, blank=True, verbose_name=u'Imagen producto')
    manufacturer=models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name=u'Fabricante')
    type_model=models.CharField(max_length=20, choices=TYPE_MANUFACTURER, verbose_name=u'Tipo de modelo')
    

    
    def __str__(self):
        return str('%s %s' % (self.manufacturer, self.model))  

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        
        

class PassiveDevices(models.Model):
    creation_date=models.DateField(auto_now_add=True,verbose_name=u'Fecha de registro')
    name=models.CharField('Nombre activo',max_length=150)
    date_purchase=models.DateField(verbose_name=u'Fecha de compra',blank=True,null=True)
    state=models.CharField(max_length=20, choices=STATES, default="Por definir",verbose_name=u'Estado')
    inventory_number=models.IntegerField('Número de inventario',unique=True)
    description=models.TextField('Observaciones',max_length=5000,blank=True,null=True)
    location=models.CharField('Ubicación',max_length=150)
    type_devices = models.ForeignKey(TypeDevices, on_delete=models.CASCADE,verbose_name=u'Tipo dispositivo')
    serial_number=models.CharField('Número de serie',max_length=150,unique=True)
    manufacturer=models.ForeignKey(ModelManufacturer, on_delete=models.CASCADE, verbose_name=u'Fabricante - Modelo')


    def __str__(self):
        return str('%s %s' % (self.manufacturer, self.name))


    class Meta:
        verbose_name = "Dispositivo Pasivo"
        verbose_name_plural = "Dispositivos Pasivos"
        
        
class Computers(models.Model):
    creation_date=models.DateField(auto_now_add=True,verbose_name=u'Fecha de registro')
    name=models.CharField('Nombre',max_length=150)
    date_purchase=models.DateField(verbose_name=u'Fecha de compra',blank=True,null=True)
    product_number=models.CharField('Número de producto',max_length=150)
    inventory_number=models.IntegerField('Número de inventario',unique=True)
    serial_number=models.CharField('Número de serie',max_length=150,unique=True)
    manufacturer=models.ForeignKey(ModelManufacturer, on_delete=models.CASCADE, null=True, blank=True,verbose_name=u'Fabricante - Modelo')
    state=models.CharField(max_length=20, choices=STATES, default="Por definir", verbose_name=u'Estado')
    processor=models.CharField('Procesador',max_length=500,blank=True,null=True)
    ram_memory=models.CharField('Memoria RAM',max_length=500,blank=True,null=True)
    disk_memory=models.CharField('Disco Duro',max_length=500,blank=True,null=True)
    graphics=models.CharField('Tarjeta gráfica',max_length=500,blank=True,null=True)
    monitor_screen=models.CharField('Pantalla',blank=True,null=True,max_length=500,)
    operative_system=models.CharField('Sistema Operativo',max_length=500,blank=True,null=True)
    description=models.TextField('Observaciones',max_length=5000,blank=True,null=True)
           
    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = "Computador"
        verbose_name_plural = "Computadores"
        


    
class EquipmentMaintenance(models.Model):
    creation_date=models.DateField(auto_now_add=True,verbose_name=u'Fecha de registro')
    computer=models.ForeignKey(Computers, on_delete=models.CASCADE,verbose_name=u'Computador')
    maintenance_type=models.CharField(max_length=20, choices=TYPE_MAINTENANCE, default="Por definir",verbose_name=u'Tipo Proceso')
    start_maintenance=models.DateField(verbose_name=u'Fecha de inicio mantenimiento')
    end_maintenance=models.DateField(verbose_name=u'Fecha de fin mantenimiento',blank=True,null=True)
    solution_description=models.TextField('Mantenimiento y solución',max_length=5000,blank=True,null=True)
    problem_description=models.TextField('Problema y condiciones iniciales',max_length=5000,blank=True,null=True)
    added_parts=models.TextField('Piezas añadidas',max_length=5000,blank=True,null=True)
    description=models.TextField('Observaciones',max_length=5000,blank=True,null=True)
    priority=models.CharField(max_length=20, choices=PRIORITY, default="Por definir",verbose_name=u'Prioridad')
    maintenance_state=models.CharField(max_length=20, choices=STATE_PROCESS, default="Pendiente", verbose_name=u'Estado Proceso')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Encargado')



    def __str__(self):
        return self.solution_description   

    class Meta:
        verbose_name = "Mantenimiento Equipo"
        verbose_name_plural = "Mantenimientos Equipos"
        

class DevicesMaintenance(models.Model):
    creation_date=models.DateField(auto_now_add=True,verbose_name=u'Fecha de registro')
    device=models.ForeignKey(PassiveDevices, on_delete=models.CASCADE, null=True, blank=True,verbose_name=u'Computador')
    maintenance_type=models.CharField(max_length=20, choices=TYPE_MAINTENANCE, default="Por definir", blank=True,null=True,verbose_name=u'Tipo Proceso')
    start_maintenance=models.DateField(verbose_name=u'Fecha de inicio mantenimiento',blank=True,null=True)
    end_maintenance=models.DateField(verbose_name=u'Fecha de fin mantenimiento',blank=True,null=True)
    solution_description=models.TextField('Mantenimiento y solución',max_length=5000,blank=True,null=True)
    problem_description=models.TextField('Problema y condiciones iniciales',max_length=5000,blank=True,null=True)
    added_parts=models.TextField('Piezas añadidas',max_length=5000,blank=True,null=True)
    description=models.TextField('Observaciones',max_length=5000,blank=True,null=True)
    priority=models.CharField(max_length=20, choices=PRIORITY, default="Por definir", blank=True,null=True,verbose_name=u'Prioridad')
    maintenance_state=models.CharField(max_length=20, choices=STATE_PROCESS, default="Pendiente", blank=True,null=True,verbose_name=u'Estado Proceso')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Encargado',blank=True,null=True)



    def __str__(self):
        return self.solution_description   

    class Meta:
        verbose_name = "Mantenimiento Dispositivo"
        verbose_name_plural = "Mantenimientos Dispositivos"
        

class Monitors(models.Model):
    creation_date=models.DateField(auto_now_add=True,verbose_name=u'Fecha de registro')
    name=models.CharField('Nombre',max_length=150)
    date_purchase=models.DateField(verbose_name=u'Fecha de compra',blank=True,null=True)
    product_number=models.CharField('Número de producto',max_length=150)
    inventory_number=models.IntegerField('Número de inventario',unique=True)
    serial_number=models.CharField('Número de serie',max_length=150,unique=True)
    manufacturer=models.ForeignKey(ModelManufacturer, on_delete=models.CASCADE, verbose_name=u'Fabricante')
    state=models.CharField(max_length=20, choices=STATES, default="Por definir", verbose_name=u'Estado')
    description=models.TextField('Observaciones',max_length=5000,blank=True,null=True)
    screen=models.IntegerField('Pulgadas',default="18")


    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitores"