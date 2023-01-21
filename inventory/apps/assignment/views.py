from datetime import datetime
from django.shortcuts import redirect
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
		if form.is_valid():
			form.save()
			if form.cleaned_data['computers'] is not None:
				Computers.objects.filter(id= form.cleaned_data['computers'].id).update(state="Activo asignado")
			
			if form.cleaned_data['monitor'] is not None:
				Monitors.objects.filter(id= form.cleaned_data['monitor'].id).update(state="Activo asignado")
			
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
	queryset = AssignUsers.objects.all()
	success_message = '¡El registro fue actualizado correctamente!'
	error_message = 'No se actualizó el registro'
 
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