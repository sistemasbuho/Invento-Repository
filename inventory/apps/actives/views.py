from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView , CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy,reverse
from .models import *
from .forms import *
from apps.assignment.models import AssignUsers, UserData
from datetime import datetime


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
    form_class = FormComputerRegister
    template_name = 'actives/register_computers.html'
    success_url = reverse_lazy('actives:visualize')
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
    form_class = FormDevicesRegister
    template_name = 'actives/register_devices.html'
    success_url = reverse_lazy('actives:visualize_devices')


class registerManufacturer(registerComputer):
    model = Manufacturer
    form_class = FormManufacturerRegister
    template_name = 'actives/register_manufacturer.html'
    success_url = reverse_lazy('actives:register_manufacturer')

class registerMonitor(registerComputer):
    model = Monitors
    form_class = FormMonitorRegister
    template_name = 'actives/register_monitor.html'
    success_url = reverse_lazy('actives:visualize_monitors')
 

def registerModelImage(request):  
    template_name = 'actives/register_model.html'
    success_message='Se ha creado con éxito'
    error_message = 'No se guardó con éxito.'
    form = FormModelManufacturerRegister()
    if request.method == 'POST':  
        form = FormModelManufacturerRegister(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()
            messages.success(request, success_message, extra_tags='God Job')
  
            return redirect("actives:register_model")
        else:
            lista = ""
            error_string = ' '
  
            for error in form.errors:
                lista+=str(error)
                error_string = ' '.join(form.errors[lista])
    
            messages.error(request, (error_message, error_string), extra_tags='Error')
    
    return render(request, template_name, {'form': form})  


class registerMaintenance(registerComputer):
    model = EquipmentMaintenance
    form_class = FormMaintenanceRegister
    template_name = 'actives/register_maintenance.html'
    success_url = reverse_lazy('actives:register_maintenance')
 
 
class registerTypes(registerComputer):
    model = TypeDevices
    form_class = FormTypesRegister
    template_name = 'actives/register_type.html'
    success_url = reverse_lazy('actives:visualize_devices')


class ListComputers(ListView):
    model = Computers
    template_name = 'actives/visualize_computers.html'
    context_object_name = 'computer_list'  
    queryset = Computers.objects.all()

class ListMonitors(ListView):
    model = Monitors
    template_name = 'actives/visualize_monitors.html'
    context_object_name = 'monitor_list'  
    queryset = Monitors.objects.all()

class ListDevices(ListView):
    model = PassiveDevices
    template_name = 'actives/visualize_devices.html'
    context_object_name = 'devices_list'  
    queryset = PassiveDevices.objects.all()


class ListMaintenance(ListView):
    model = EquipmentMaintenance
    template_name = 'actives/visualize_maintenance.html'
    context_object_name = 'devices_list'  
    queryset = EquipmentMaintenance.objects.all()

    
class ComputersDetailView(ListView):
    model = Computers
    template_name = 'actives/details_pc.html'

    def get_context_data(self, **kwargs):
        context = super(ComputersDetailView, self).get_context_data(**kwargs)
        context['second_queryset'] =Computers.objects.filter(id = self.kwargs['pk'])
        context['third_queryset'] = EquipmentMaintenance.objects.filter(computer = self.kwargs['pk'])
        context['assign_queryset'] = AssignUsers.objects.filter(computers = self.kwargs['pk'])

        return context


class DevicesDetailView(ListView):
    model = PassiveDevices
    template_name = 'actives/details_devices.html'

    def get_context_data(self, **kwargs):
        context = super(DevicesDetailView, self).get_context_data(**kwargs)
        context['second_queryset'] =PassiveDevices.objects.filter(id = self.kwargs['pk'])
        context['third_queryset'] = DevicesMaintenance.objects.filter(device = self.kwargs['pk'])
        context['assign_queryset'] = AssignUsers.objects.filter(passive_devices = self.kwargs['pk'])

        return context


class MonitorDetailView(ListView):
    model = Monitors
    template_name = 'actives/details_monitor.html'

    def get_context_data(self, **kwargs):
        context = super(MonitorDetailView, self).get_context_data(**kwargs)
        context['second_queryset'] = Monitors.objects.filter(id = self.kwargs['pk'])
        context['third_queryset'] = DevicesMaintenance.objects.filter(device = self.kwargs['pk'])
        context['assign_queryset'] = AssignUsers.objects.filter(monitor = self.kwargs['pk'])

        return context


class UpdateComputer(_FormValid,UpdateView):
    model = Computers
    template_name = 'actives/update_computer.html'
    context_object_name = 'computer_list'
    form_class = FormComputerRegister  
    queryset = Computers.objects.all()
    success_message = '¡El registro fue actualizado correctamente!'
    error_message = 'No se actualizó el registro'
 
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("actives:update_computer", kwargs={"pk": pk})


class UpdateDevice(UpdateComputer):
    model = PassiveDevices
    template_name = 'actives/update_device.html'
    context_object_name = 'devices_list'
    form_class = FormDevicesRegister  
    queryset = PassiveDevices.objects.all()
 
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("actives:update_device", kwargs={"pk": pk})


class UpdateMonitor(UpdateComputer):
    model = Monitors
    template_name = 'actives/update_monitor.html'
    context_object_name = 'monitor_list'
    form_class = FormMonitorRegister  
    queryset = Monitors.objects.all()
 
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("actives:update_monitor", kwargs={"pk": pk})


@login_required
@permission_required('actives.add_actives', raise_exception=True)
def dashboardGeneral (request):
    today=datetime.today()

    computers=Computers.objects.all().count()
    devices=PassiveDevices.objects.all().count()
    monitor=Monitors.objects.all().count()
    users=UserData.objects.all().count()
    maintenance = EquipmentMaintenance.objects.filter(start_maintenance__year=today.year, start_maintenance__month=today.month)
    assignment = AssignUsers.objects.filter(date_assignment__year=today.year, date_assignment__month=today.month)

    return render(request,'home/index.html',{
     
        'computers':computers,
        'devices':devices,
        'monitors':monitor, 
        'users':users, 
        'maintenance':maintenance,
        'assignment':assignment,
        
        })
 