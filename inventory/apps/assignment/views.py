from django.contrib.auth.decorators import login_required,permission_required
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import ListView , CreateView,  View
from django.shortcuts import get_object_or_404
from django.urls import reverse,reverse_lazy
from .models import *
from .forms import *
from apps.actives.views import registerComputer,ComputersDetailView

class ListUsers(ListView):
	model = AssignUsers
	template_name = 'assignment/visualize_users.html'
	context_object_name = 'users_list'  
	queryset = AssignUsers.objects.all()
 

class registerUser(registerComputer):
	model = AssignUsers
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


class UserDetailView(DetailView):
	model = AssignUsers

	def get_queryset(self):
		query = super(UserDetailView, self).get_queryset()
		return query

	def get(self, request, *args, **kwargs):
		book = get_object_or_404(AssignUsers, pk=kwargs['pk'])
		context = {'user_list': book}
		return render(request, 'assignment/details_user.html', context)