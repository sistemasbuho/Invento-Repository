from django.shortcuts import render
import os
from django.contrib.auth.decorators import login_required,permission_required
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import ListView , CreateView,  View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse,reverse_lazy
from .models import *
from .forms import *


# Clase privada de la que heredan todas las vistas-----------------------------------		
class _FormValid(PermissionRequiredMixin):
	model = Computers
	permission_required = 'idea.add_idea'
	form_class = FormComputerRegister
	template_name = 'idea/register.html'
	success_url = reverse_lazy('dashboard')
	success_message = 'Se ha creado con éxito'
	error_message = 'No se guardo con exito.'

	def form_valid(self, form):
		messages.success(self.request, self.success_message, extra_tags='God Job')
		return super().form_valid(form)

	def form_invalid(self, form):
		lista = ""
		for error in form.errors:
			lista+=str(error)

		#https://stackoverflow.com/questions/43588876/how-can-i-add-additional-data-to-django-messages
		messages.error(self.request, '%s debido a un error en el campo de: %s' % (self.error_message, lista), extra_tags='Error')
		return redirect(str(self.success_url))


	#Validación que limpia el los input de un espacio inicial y final con strip al guardar
	#https://www.peterbe.com/plog/automatically-strip-whitespace-in-django-forms
	def clean(self):
		for field in self.cleaned_data:
			if isinstance(self.cleaned_data[field], basestring):
				self.cleaned_data[field] = self.cleaned_data[field].strip()
		return self.cleaned_data


class registerComputer(_FormValid,CreateView):
	model = Computers
	# permission_required = 'idea.add_idea'
	form_class = FormComputerRegister
	template_name = 'actives/register_computers.html'
	success_url = reverse_lazy('actives:register')
	success_message = '¡El registro fue creado correctamente!'
	error_message = 'No se guardo con exito.'

	#n+1 solucionado
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST) #cargo los datos del formulario
		form_header = dict(request.POST.lists())

		 
		if form.is_valid():
			form.save()
			return self.form_valid(form)

		#De lo contrario que muestre error
		else:
			self.form_invalid(form)
		return redirect(str(self.success_url))



class registerDevices(_FormValid,CreateView):
	model = Computers
	# permission_required = 'idea.add_idea'
	form_class = FormComputerRegister
	template_name = 'actives/register_computers.html'
	success_url = reverse_lazy('actives:register')
	success_message = '¡El registro fue creado correctamente!'
	error_message = 'No se guardo con exito.'

	#n+1 solucionado
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST) #cargo los datos del formulario
		form_header = dict(request.POST.lists())

		 
		if form.is_valid():
			form.save()
			return self.form_valid(form)

		#De lo contrario que muestre error
		else:
			self.form_invalid(form)
		return redirect(str(self.success_url))





class ListComputers(ListView):
	model = Computers
	template_name = 'actives/visualize_computers.html'
	context_object_name = 'computer_list'   # your own name for the list as a template variable
	queryset = Computers.objects.all()
