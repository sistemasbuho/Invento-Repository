from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

	path('register/', registerComputer.as_view(), name='register'),
 	path('register/maintenance/computer/', registerMaintenance.as_view(), name='register_maintenance_computer'),
   	path('register/maintenance/device/', registerMaintenanceDevices.as_view(), name='register_maintenance_device'),
 	path('register/maintenance/monitor/', registerMaintenanceMonitor.as_view(), name='register_maintenance_monitor'),

    path('register/manufacturer/', registerManufacturer.as_view(), name='register_manufacturer'),
    path('register/model/', registerModelImage, name='register_model'),
    path('register/type/', registerTypes.as_view(), name='register_type'),
   	path('register/devices/', registerDevices.as_view(), name='register_devices'),
   	path('register/monitor/', registerMonitor.as_view(), name='register_monitor'),


 	path('update/computer/<int:pk>', UpdateComputer.as_view(), name='update_computer'),
   	path('update/device/<int:pk>', UpdateDevice.as_view(), name='update_device'),
   	path('update/monitor/<int:pk>', UpdateMonitor.as_view(), name='update_monitor'),
    path('update/monitor/maintenance/<int:pk>', UpdateMonitorMaintenance.as_view(), name='update_monitor_maintenance'),
    path('update/computer/maintenance/<int:pk>', UpdateComputerMaintenance.as_view(), name='update_computer_maintenance'),
    path('update/device/maintenance/<int:pk>', UpdateDeviceMaintenance.as_view(), name='update_device_maintenance'),



 	path('list/', ListComputers.as_view(), name='visualize'),
 	path('list/devices/', ListDevices.as_view(), name='visualize_devices'),
 	path('list/maintenance/', ListMaintenance.as_view(), name='visualize_maintenance'),
 	path('list/monitor/', ListMonitors.as_view(), name='visualize_monitors'),

    
    path('details/computer/<int:pk>', ComputersDetailView.as_view(), name='details_computer'),
    path('details/device/<int:pk>', DevicesDetailView.as_view(), name='details_device'),
    path('details/monitor/<int:pk>', MonitorDetailView.as_view(), name='details_monitor'),


    path('', dashboardGeneral, name='dashboard'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)