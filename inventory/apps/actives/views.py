
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView , CreateView, View
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


# Clase privada de la que heredan todas las vistas-----------------------------------		
class _FormValid(PermissionRequiredMixin):
	model = Computers
	permission_required = 'idea.add_idea'
	form_class = FormComputerRegister
	success_message = 'Se ha creado con éxito'
	error_message = 'No se guardó con éxito.'

	def form_valid(self, form):
		messages.success(self.request, self.success_message, extra_tags='God Job')
		return super().form_valid(form)

	def form_invalid(self, form):
		lista = ""
		error_string = ' '
  
		for error in form.errors:
			lista+=str(error)
			error_string = ' '.join(form.errors[lista])
  
		messages.error(self.request, (self.error_message, error_string), extra_tags='Error')
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
 
		if form.is_valid():
			form.save()
			return self.form_valid(form)

		#De lo contrario que muestre error
		else:
			self.form_invalid(form)
		return redirect(str(self.success_url))


class registerDevices(registerComputer):
	model = PassiveDevices
	# permission_required = 'idea.add_idea'
	form_class = FormDevicesRegister
	template_name = 'actives/register_devices.html'
	success_url = reverse_lazy('actives:register_devices')


class registerManufacturer(registerComputer):
	model = Manufacturer
	# permission_required = 'idea.add_idea'
	form_class = FormManufacturerRegister
	template_name = 'actives/register_manufacturer.html'
	success_url = reverse_lazy('actives:register_manufacturer')

 
class registerModel(registerComputer):
	model = ModelManufacturer
	# permission_required = 'idea.add_idea'
	form_class = FormModelManufacturerRegister
	template_name = 'actives/register_model.html'
	success_url = reverse_lazy('actives:register_model')


class registerTypes(registerComputer):
	model = TypeDevices
	# permission_required = 'idea.add_idea'
	form_class = FormTypesRegister
	template_name = 'actives/register_type.html'
	success_url = reverse_lazy('actives:register_type')


class ListComputers(ListView):
	model = Computers
	template_name = 'actives/visualize_computers.html'
	context_object_name = 'computer_list'  
	queryset = Computers.objects.all()


class ListDevices(ListView):
	model = PassiveDevices
	template_name = 'actives/visualize_devices.html'
	context_object_name = 'devices_list'  
	queryset = PassiveDevices.objects.all()


    
class ComputersDetailView(DetailView):
	model = Computers

	def get_queryset(self):
		query = super(ComputersDetailView, self).get_queryset()
		return query

	def get(self, request, *args, **kwargs):
		book = get_object_or_404(Computers, pk=kwargs['pk'])
		context = {'computers_list': book}
		return render(request, 'actives/details_pc.html', context)