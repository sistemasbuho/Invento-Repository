from django.urls import path
from .views import *

urlpatterns = [

	path('register/', registerComputer.as_view(), name='register'),
 	path('list/', ListComputers.as_view(), name='visualize'),

]