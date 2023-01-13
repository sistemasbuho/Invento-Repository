from django.urls import path
from .views import *

urlpatterns = [

	path('register/', registerComputer.as_view(), name='register'),
 	path('list/', ListComputers.as_view(), name='visualize'),
  	path('register/devices/', registerDevices.as_view(), name='register_devices'),
 	path('list/devices/', ListDevices.as_view(), name='visualize_devices'),
    path('register/manufacturer/', registerManufacturer.as_view(), name='register_manufacturer'),
    path('register/model/', registerModel.as_view(), name='register_model'),
    path('register/type/', registerTypes.as_view(), name='register_type'),
    path('details/computer/<int:pk>', ComputersDetailView.as_view(), name='details_computer'),


]