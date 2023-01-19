from django import forms
from .models import *


class FormComputerRegister(forms.ModelForm):
	class Meta:
		model = Computers
		fields=['name','date_purchase','product_number','inventory_number','manufacturer','serial_number','state',
                'processor','ram_memory','disk_memory','graphics','monitor_screen','operative_system','description']
  
		widgets = {
			'name':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'PC - Placa asignada ',
					'id':'name' }),
   
			'date_purchase':forms.DateInput(
			       format=('%Y-%m-%d'),
       		 	attrs={
               'class': 'form-control', 
               'placeholder': 'yy-mm-dd',
               'type': 'date'}),
			
			'product_number':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Ej: T1B43LT',
					'id':'product_number' }),
			
			'inventory_number':forms.NumberInput(
				attrs={
					'class':'form-control',
					'placeholder':'Placa asignada',
					'id':'inventory_number' }),
	
            'serial_number':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Ej: 5CD61520YC',
					'id':'description',	
			}),
            
            'manufacturer':forms.Select(
				attrs={
					'class':'form-control',
					'id':'manufacturer', }),
             
            'state':forms.Select(
				attrs={
					'class':'form-control',
					'id':'state', }),
            
            'processor':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Marca Generación-Modelo Ej: Intel Core i9-12950HX',
					'id':'processor' }),
            
        	'ram_memory':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'#GB - Slots Ej: 8GB-2x4',
					'id':'ram_memory' }),
         
         	'disk_memory':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Tipo - Capacidad Ej: SSD - 500GB',
					'id':'disk_memory' }),

		         
         	'graphics':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Marca Modelo Ej: NVIDIA GeForce RTX 3070 Ti (8 GB)',
					'id':'graphics' }),
        
                 
         	'disk_memory':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Tipo - Capacidad  Ej: M.2 - 250GB',
					'id':'disk_memory' }),
                 
         	'monitor_screen':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Pulgadas - Estado - Tipo Ej: 14"-Original-Táctil',
					'id':'monitor_screen' }),
          
            'operative_system':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Marca Versión Tipo Ej: Windows 10 Home',
					'id':'operative_system' }),
              
            'description':forms.Textarea(
				attrs={
					'class':'form-control',
					'placeholder':'Puede incluir cualquier otra característica: Rayones, defectos de carcasa, dispositivos incluidos, fallas incorregibles, lector de huellas , etc',
					'id':'description', 
					'rows':5, 
     			}),
	}

	def clean_model(self):
		serial_number = self.cleaned_data["serial_number"]
		if Computers.objects.filter(serial_number=serial_number).exists():
			raise forms.ValidationError('El registro %s ya existe' % serial_number)    
		return serial_number


class FormMonitorRegister(forms.ModelForm):
	class Meta:
		model = Monitors
		fields=['name','date_purchase','product_number','inventory_number','manufacturer','serial_number','state',
                'description','screen']
  
		widgets = {
			'name':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'PC - Placa asignada ',
					'id':'name' }),
   
			'date_purchase':forms.DateInput(
			       format=('%Y-%m-%d'),
       		 	attrs={
               'class': 'form-control', 
               'placeholder': 'yy-mm-dd',
               'type': 'date'}),
			
			'product_number':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Ej: T1B43LT',
					'id':'product_number' }),
			
			'inventory_number':forms.NumberInput(
				attrs={
					'class':'form-control',
					'placeholder':'Placa asignada',
					'id':'inventory_number' }),
   
   			'screen':forms.NumberInput(
				attrs={
					'class':'form-control',
					'placeholder':'Pulgadas',
					'id':'screen' }),
	
            'serial_number':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Ej: 5CD61520YC',
					'id':'description',	
			}),
            
            'manufacturer':forms.Select(
				attrs={
					'class':'form-control',
					'id':'manufacturer', }),
             
            'state':forms.Select(
				attrs={
					'class':'form-control',
					'id':'state', }),

            'description':forms.Textarea(
				attrs={
					'class':'form-control',
					'placeholder':'Puede incluir cualquier otra característica: Rayones, defectos de carcasa, dispositivos incluidos, fallas incorregibles, lector de huellas , etc',
					'id':'description', 
					'rows':5, 
     			}),
	}

	def clean_model(self):
		serial_number = self.cleaned_data["serial_number"]
		if Computers.objects.filter(serial_number=serial_number).exists():
			raise forms.ValidationError('El registro %s ya existe' % serial_number)    
		return serial_number

        
class FormManufacturerRegister(forms.ModelForm):
	class Meta:
		model = Manufacturer
		fields=['name','type_manufacturer']
  
		widgets = {
				'name':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Nombre del fabricante',
					'onkeyup':'this.value = this.value.toUpperCase();',
					'id':'name' }),
    
				     
				'type_manufacturer':forms.Select(
					attrs={
						'class':'form-control',
						'id':'type_manufacturer', }),

		}

	def clean_name(self):
		name = self.cleaned_data["name"]
		if Manufacturer.objects.filter(name=name).exists():
			raise forms.ValidationError('El registro %s ya existe' % name)    
		return name


class FormModelManufacturerRegister(forms.ModelForm):
	class Meta:
		model = ModelManufacturer
		fields=['model','type_model','product_image','manufacturer']
  
		widgets = {
				'model':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Modelo Ej: Notebook 678',
					'id':'model' }),
    
				     
				'type_model':forms.Select(
					attrs={
						'class':'form-control',
						'id':'type_model', }),
				
    			'manufacturer':forms.Select(
					attrs={
						'class':'form-control',
						'id':'manufacturer', }),
		}

	def clean_model(self):
		model = self.cleaned_data["model"]
		if ModelManufacturer.objects.filter(model=model).exists():
			raise forms.ValidationError('El registro %s ya existe' % model)    
		return model
  

class FormDevicesRegister(forms.ModelForm):
	class Meta:
		model = PassiveDevices
		fields=['description','name','state','date_purchase','inventory_number','location','type_devices','serial_number','manufacturer']
  
		widgets = {
				'name':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Tipo - Placa : Ej: MOU-45, TEC-32',
					'id':'name' }),
    
    			'date_purchase':forms.DateInput(
			       format=('%Y-%m-%d'),
					attrs={
				'class': 'form-control', 
				'placeholder': 'yy-mm-dd',
				'type': 'date'}),

				'state':forms.Select(
					attrs={
						'class':'form-control',
						'id':'state', }),
				
    			'manufacturer':forms.Select(
					attrs={
						'class':'form-control',
						'id':'manufacturer', }),
				
					
				'inventory_number':forms.NumberInput(
					attrs={
						'class':'form-control',
						'placeholder':'Placa asignada',
						'id':'inventory_number', }),
    
    			'location':forms.TextInput(
					attrs={
						'class':'form-control',
      					'placeholder':'Oficina - Asignado',
						'id':'location', }),
       
				'type_devices':forms.Select(
					attrs={
						'class':'form-control',
						'id':'type_devices', }),
    
				'serial_number':forms.TextInput(
					attrs={
						'class':'form-control',
      					'placeholder':'Ej: 5CD61520YC',
						'id':'location', }),
    
               'description':forms.Textarea(
				attrs={
					'class':'form-control',
					'placeholder':'Puede incluir cualquier otra característica: Rayones, defectos de fábrica, dispositivos incluidos, fallas incorregibles, etc',
					'id':'description', 
					'rows':5, 
     			}),
		}
  
  
class FormTypesRegister(forms.ModelForm):
	class Meta:
		model = TypeDevices
		fields=['name']
  
		widgets = {
				'name':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Tipo de dispositivo',
					'onkeyup':'this.value = this.value.toUpperCase();',
					'id':'name' }),
		}
  
	def clean_name(self):
		name = self.cleaned_data["name"]
		if TypeDevices.objects.filter(name=name).exists():
			raise forms.ValidationError('El registro %s ya existe' % name)    
		return name


class FormMaintenanceRegister(forms.ModelForm):
	class Meta:
		model = EquipmentMaintenance
		fields=['computer','maintenance_type','start_maintenance','end_maintenance','solution_description','problem_description','added_parts','description','priority','maintenance_state']
  
		widgets = {
				'computer':forms.Select(
				attrs={
					'class':'form-control',
					'placeholder':'',
					'id':'computer' }),
    
    			'priority':forms.Select(
				attrs={
					'class':'form-control',
					'placeholder':'',
					'id':'priority' }),
    
    			'maintenance_state':forms.Select(
				attrs={
					'class':'form-control',
					'placeholder':'',
					'id':'maintenance_state' }),


				'maintenance_type':forms.Select(
							attrs={
								'class':'form-control',
								'placeholder':'Tipo de mantenimiento',
								'id':'maintenance_type' }),
    
    			'user':forms.Select(
							attrs={
								'class':'form-control',
								'placeholder':'',
								'id':'user' }),
     
				
    			'start_maintenance':forms.DateInput(
							format=('%Y-%m-%d'),
								attrs={
								'class': 'form-control', 
								'placeholder': 'yy-mm-dd',
								'type': 'date'}),
       
				'end_maintenance':forms.DateInput(
						format=('%Y-%m-%d'),
							attrs={
							'class': 'form-control', 
							'placeholder': 'yy-mm-dd',
							'type': 'date'}),
    
    			'description':forms.Textarea(
				attrs={
					'class':'form-control',
					'placeholder':'Puede incluir cualquier otra característica: Rayones, defectos de fábrica, dispositivos incluidos, fallas incorregibles, etc',
					'id':'description', 
					'rows':5, 
     			}),
          
                'solution_description':forms.Textarea(
				attrs={
					'class':'form-control',
					'placeholder':'Describa de manera técnica, la solución dada al problema',
					'id':'solution_description', 
					'rows':5, 
     			}),
             
                'problem_description':forms.Textarea(
				attrs={
					'class':'form-control',
					'placeholder':'Describa el problema de manera técnica, en que condiciones recibe el equipo',
					'id':'problem_description', 
					'rows':5, 
     			}),
                
                'added_parts':forms.Textarea(
				attrs={
					'class':'form-control',
					'placeholder':'Incluya todas las piezas añadidas, cambiadas o removidas para este mantenimiento',
					'id':'added_parts', 
					'rows':5, 
     			}),
		}
