from django import forms
from .models import *
from django.contrib.auth.models import User


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
		fields=['user','assignment','date_assignment','computers','passive_devices']
  
		widgets = {
			'user':forms.Select(
				attrs={
					'class':'form-control',
					'id':'manufacturer', }),
   
      
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
  
  
class FormAssignUpdate(forms.ModelForm):
	class Meta:
		model = AssignUsers
		fields=['user','assignment','date_assignment','computers','passive_devices']
  
		widgets = {
			'user':forms.Select(
				attrs={
					'class':'form-control',
					'id':'manufacturer', }),
   
      
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