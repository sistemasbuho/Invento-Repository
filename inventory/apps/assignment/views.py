from datetime import datetime
from django.shortcuts import redirect,render
from django.views.generic import ListView ,  UpdateView,View
from django.urls import reverse,reverse_lazy
from .models import *
from .forms import *
from apps.actives.views import registerComputer,_FormValid
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class ListUsers(ListView):
	model = AssignUsers
	template_name = 'assignment/visualize_users.html'
	context_object_name = 'users_list'  
	queryset = AssignUsers.objects.all()
 

class registerUser(registerComputer):
	model = UserData
	form_class = FormUserRegister
	template_name = 'assignment/register_users.html'
	success_url = reverse_lazy('users:visualize_users')


class registerAssign(registerComputer):
	model = AssignUsers
	form_class = FormAssignRegister
	template_name = 'assignment/assign_user.html'
	success_url = reverse_lazy('users:visualize_users')

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		form_header = dict(request.POST.lists())

		# Realizamos el guardado del many to many añadiendo desde una lista
		validate_passive_devices = 'passive_devices' in form_header
		if validate_passive_devices:
			passive_devices_query = PassiveDevices.objects.filter(pk__in=form_header['passive_devices'])  # ['2', '3']
			form.fields['passive_devices'].queryset = passive_devices_query
  
		if form.is_valid():
			form.save()
			if form.cleaned_data['computers'] is not None:
				Computers.objects.filter(id= form.cleaned_data['computers'].id).update(state="Activo asignado")
			
			if form.cleaned_data['monitor'] is not None:
				Monitors.objects.filter(id= form.cleaned_data['monitor'].id).update(state="Activo asignado")
			
			# TODO: traer los dispositivo y actualizamos su estado
			if validate_passive_devices:		
				PassiveDevices.objects.filter(pk__in=form_header['passive_devices']).update(state="Activo asignado")
				
			return self.form_valid(form)

		else:
			self.form_invalid(form)
		return redirect(str(self.success_url))


class UserDetailView(ListView):
	model = AssignUsers
	template_name = 'assignment/details_user.html'

	def get_context_data(self, **kwargs):
		context = super(UserDetailView, self).get_context_data(**kwargs)
		context['user_list_assign'] =AssignUsers.objects.filter(id = self.kwargs['pk'])
		# context['third_queryset'] = DevicesMaintenance.objects.filter(device = self.kwargs['pk'])
		return context


class UpdateAssigment(_FormValid,UpdateView):
	model = AssignUsers
	template_name = 'assignment/update_assign.html'
	context_object_name = 'user_list'
	form_class = FormAssignUpdate  
	success_message = '¡El registro fue actualizado correctamente!'
	error_message = 'No se actualizó el registro'

	def get_form(self,*args,**kwargs):
		instance = self.get_object()
		form = self.form_class(instance=instance)
		form.fields['passive_devices'].queryset = instance.passive_devices.all() 
		return form

	def post(self,request,*args,**kwargs):
		form_header = dict(request.POST.lists())
  
		if 'passive_devices' not in form_header:
			#capturo los ids de actor (manytomany)
			passive_devices_query = PassiveDevices.objects.none()

		else:
			#sino capturo todo los valores
			passive_devices_query = PassiveDevices.objects.filter(pk__in=form_header['passive_devices']) 

		#cargo los datos del formulario
		form = self.form_class(request.POST, instance = self.get_object()) #get_object: hace una petición get para obtener el id para no usar una consulta
		form.fields['passive_devices'].queryset = passive_devices_query

		if form.is_valid():

   			# capturamos los datos del formulario inicial
			get_form_start = self.get_form(self)
			pasivo_original = get_form_start.fields['passive_devices'].queryset
			
			try:
				pasivo_actualizado = PassiveDevices.objects.filter(pk__in=form_header['passive_devices'])
			except KeyError:
				pasivo_actualizado = PassiveDevices.objects.none()
    
			_difference = set(pasivo_original).difference(set(pasivo_actualizado))

			if _difference:
				for device in _difference:
					PassiveDevices.objects.filter(pk=device.id).update(state="Activo disponible")

			else:
				PassiveDevices.objects.filter(pk__in=form_header['passive_devices']).update(state="Activo asignado")
			
			form.save()

			return self.form_valid(form)

		else:
			self.form_invalid(form)
		return redirect(str(self.success_url))


	def get_success_url(self):
		pk = self.kwargs["pk"]
		return reverse("users:detail_users", kwargs={"pk": pk})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('assignment/generate_act.html', data)
        return HttpResponse(pdf, content_type='application/pdf')