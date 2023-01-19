from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

	path('register/', registerComputer.as_view(), name='register'),
 	path('register/maintenance/', registerMaintenance.as_view(), name='register_maintenance'),
    path('register/manufacturer/', registerManufacturer.as_view(), name='register_manufacturer'),
    path('register/model/', registerModel.as_view(), name='register_model'),
    path('register/type/', registerTypes.as_view(), name='register_type'),
   	path('register/devices/', registerDevices.as_view(), name='register_devices'),

 	path('update/computer/<int:pk>', UpdateComputer.as_view(), name='update_computer'),
   	path('update/device/<int:pk>', UpdateDevice.as_view(), name='update_device'),

 	path('list/', ListComputers.as_view(), name='visualize'),
 	path('list/devices/', ListDevices.as_view(), name='visualize_devices'),
 	path('list/maintenance/', ListMaintenance.as_view(), name='visualize_maintenance'),

    
    path('details/computer/<int:pk>', ComputersDetailView.as_view(), name='details_computer'),


]