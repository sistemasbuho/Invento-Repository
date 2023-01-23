from django import forms
from .models import *
from django.contrib.auth.models import User
from apps.actives.models import Computers,Monitors,PassiveDevices
from ckeditor.widgets import CKEditorWidget

class FormUserRegister(forms.ModelForm):
	class Meta:
		model = UserData
		fields=['name_user','email_user','dni_user','type_assignment']
  
		widgets = {
		
   
   			'name_user':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Nombre y apellidos',
					'id':'name_user' }),
      
			'email_user':forms.EmailInput(
				attrs={
					'class':'form-control',
					'placeholder':'example@buho.media',
					'id':'email_user' }),
   
   			'dni_user':forms.NumberInput(
				attrs={
					'class':'form-control',
					'placeholder':'Documento de Identidad',
					'id':'dni_user' }),
            
            'type_assignment':forms.Select(
				attrs={
					'class':'form-control',
					'id':'type_assignment', }),
        }

	def clean_model(self):
		model = self.cleaned_data["email_user"]
		if AssignUsers.objects.filter(model=model).exists():
			raise forms.ValidationError('El registro %s ya existe' % model)    
		return model


class FormAssignRegister(forms.ModelForm):
	class Meta:
		model = AssignUsers
  
		fields=['monitor','user','assignment','date_assignment','computers','passive_devices','description']

		widgets = {
			'user':forms.Select(
				attrs={
					'class':'form-control',
					'id':'manufacturer', }),
   
      		'monitor':forms.Select(
				attrs={
					'class':'form-control',
					'id':'monitor', }),
   
			'assignment':forms.Select(
				attrs={
					'class':'form-control',
					'placeholder':'',
					'id':'email_user' }),
   
		    'date_assignment':forms.DateInput(
				format=('%Y-%m-%d'),
       		 	attrs={
               'class': 'form-control', 
               'placeholder': 'yy-mm-dd',
               'type': 'date'}),
            
            'computers':forms.Select(
				attrs={
					'class':'form-control',
					'id':'computers', }),
            
        }

	def __init__(self,*args, **kwargs):
		super(FormAssignRegister, self).__init__(*args, **kwargs)
		self.fields['passive_devices'].queryset = PassiveDevices.objects.none()
  
		self.fields['passive_devices'].required = False
		self.fields['passive_devices'].widget.attrs['class'] = "form-control"
		self.fields['passive_devices'].widget.attrs['id'] = "passive_devices_crear_id"
  
		self.fields['computers'].queryset = Computers.objects.filter(state="Activo disponible")
		self.fields['monitor'].queryset = Monitors.objects.filter(state="Activo disponible")

    

class FormAssignUpdate(forms.ModelForm):
	class Meta:
		model = AssignUsers
		fields=['monitor','user','assignment','date_assignment','computers','passive_devices','description']
  
		widgets = {
			'user':forms.Select(
				attrs={
					'class':'form-control',
					'id':'manufacturer', }),
   
   			'monitor':forms.Select(
				attrs={
					'class':'form-control',
					'id':'monitor', }),
      
			'assignment':forms.Select(
				attrs={
					'class':'form-control',
					'placeholder':'',
					'id':'email_user' }),
   
		    'date_assignment':forms.DateInput(
				format=('%Y-%m-%d'),
       		 	attrs={
               'class': 'form-control', 
               'placeholder': 'yy-mm-dd',
               'type': 'date'}),
            
            'computers':forms.Select(
				attrs={
					'class':'form-control',
					'id':'computers', }),
            
        }

	def __init__(self,*args, **kwargs):
		super(FormAssignUpdate, self).__init__(*args, **kwargs)
		self.fields['passive_devices'].queryset = PassiveDevices.objects.none()
  
		self.fields['passive_devices'].required = False
		self.fields['passive_devices'].widget.attrs['class'] = "form-control"
		self.fields['passive_devices'].widget.attrs['id'] = "passive_devices_crear_id"

		# validar uun atributo interno
		# https://stackoverflow.com/questions/610883/how-do-i-check-if-an-object-has-an-attribute
		hasattr(kwargs['instance'], 'monitor_id')

		# query_monitor_activo_disponible = Monitors.objects.filter(state="Activo disponible")
		# if kwargs['instance'].monitor:
		# 	query_monitor_pk = Monitors.objects.filter(pk=kwargs['instance'].monitor.pk)
		# 	self.fields['monitor'].queryset = query_monitor_pk.union(query_monitor_activo_disponible)
		# else:
		# 	self.fields['monitor'].queryset = query_monitor_activo_disponible