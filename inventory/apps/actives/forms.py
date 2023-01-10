from django import forms
from .models import *
from django.contrib.auth.models import User



class FormComputerRegister(forms.ModelForm):
	class Meta:
		model = Computers
		fields=['name','date_purchase','product_number','inventory_number','manufacturer','serial_number','state',
                'processor','ram_memory','disk_memory','graphics','monitor_screen','operative_system','description']
  
		widgets = {
			'name':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Nombre del equipo',
					'id':'name' }),
   
			'date_purchase':forms.DateInput(
				attrs={
					'class':'form-control',
					'placeholder':'Fecha de compra',
					'id':'date_purchase' }),
			
			'product_number':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'',
					'id':'product_number' }),
			
			'inventory_number':forms.NumberInput(
				attrs={
					'class':'form-control',
					'placeholder':'Placa asignada',
					'id':'inventory_number' }),
	
            'serial_number':forms.TextInput(
				attrs={
					'class':'form-control',
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
					'placeholder':'',
					'id':'processor' }),
            
        	'ram_memory':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'GB - Slots',
					'id':'ram_memory' }),
         
         	'disk_memory':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Tipo - Capacidad',
					'id':'disk_memory' }),

		         
         	'graphics':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'',
					'id':'graphics' }),
        
                 
         	'disk_memory':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Tipo - Capacidad',
					'id':'disk_memory' }),
                 
         	'monitor_screen':forms.NumberInput(
				attrs={
					'class':'form-control',
					'placeholder':'Pulgadas',
					'id':'monitor_screen' }),
          
            'operative_system':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'',
					'id':'operative_system' }),
              
            'description':forms.Textarea(
				attrs={
					'class':'form-control',
					'placeholder':'Puede incluir cualquier otra característica',
					'id':'description', 
					'rows':5, 
     			}),
	}


class FormManufacturerRegister(forms.ModelForm):
	class Meta:
		model = Manufacturer
		fields=['name','is_device','is_computer']
  
		widgets = {
				'name':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Nombre del fabricante',
					'id':'name' }),
    
				     
				'is_device':forms.Select(
					attrs={
						'class':'form-control',
						'id':'is_device', }),
				
					
				'is_computer':forms.Select(
					attrs={
						'class':'form-control',
						'id':'is_computer', }),
		}
  
  
class FormModelManufacturerRegister(forms.ModelForm):
	class Meta:
		model = ModelManufacturer
		fields=['model','is_device','is_computer','product_image','manufacturer']
  
		widgets = {
				'model':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Nombre del fabricante',
					'id':'model' }),
    
				     
				'is_device':forms.Select(
					attrs={
						'class':'form-control',
						'id':'is_device', }),
				
					
				'is_computer':forms.Select(
					attrs={
						'class':'form-control',
						'id':'is_computer', }),
    
    			'manufacturer':forms.Select(
					attrs={
						'class':'form-control',
						'id':'manufacturer', }),
		}
  
  
class FormDevicesRegister(forms.ModelForm):
	class Meta:
		model = PassiveDevices
		fields=['name','state','date_purchase','inventory_number','location','type_devices','serial_number','manufacturer']
  
		widgets = {
				'name':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Nombre del fabricante',
					'id':'name' }),
    
    			'date_purchase':forms.DateInput(
				attrs={
					'class':'form-control',
					'placeholder':'Fecha de compra',
					'id':'date_purchase' }),
    
				     
				'state':forms.Select(
					attrs={
						'class':'form-control',
						'id':'state', }),
				
					
				'inventory_number':forms.NumberInput(
					attrs={
						'class':'form-control',
						'id':'inventory_number', }),
    
    			'location':forms.TextInput(
					attrs={
						'class':'form-control',
						'id':'location', }),
       
				'type_devices':forms.TextInput(
					attrs={
						'class':'form-control',
						'id':'location', }),
    
				'serial_number':forms.TextInput(
					attrs={
						'class':'form-control',
						'id':'location', }),
		}