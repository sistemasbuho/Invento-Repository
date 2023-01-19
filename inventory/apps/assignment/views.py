from django.contrib.auth.decorators import login_required,permission_required
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import ListView , CreateView,  View, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse,reverse_lazy
from .models import *
from .forms import *
from apps.actives.views import registerComputer,_FormValid

class ListUsers(ListView):
	model = AssignUsers
	template_name = 'assignment/visualize_users.html'
	context_object_name = 'users_list'  
	queryset = AssignUsers.objects.all()
 

class registerUser(registerComputer):
	model = UserData
	# permission_required = 'idea.add_idea'
	form_class = FormUserRegister
	template_name = 'assignment/register_users.html'
	success_url = reverse_lazy('users:register_users')


class registerAssign(registerComputer):
	model = AssignUsers
	# permission_required = 'idea.add_idea'
	form_class = FormAssignRegister
	template_name = 'assignment/assign_user.html'
	success_url = reverse_lazy('users:assign_users')


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
		return reverse("actives:update_assignment", kwargs={"pk": pk})

