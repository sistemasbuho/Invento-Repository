from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError



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
		inventory_number = self.cleaned_data["inventory_number"]
		if Computers.objects.filter(inventory_number=inventory_number).exists():
			raise forms.ValidationError('El registro %s ya existe' % inventory_number)    
		return inventory_number

        
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