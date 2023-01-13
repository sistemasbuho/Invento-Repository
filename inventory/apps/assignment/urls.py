from django.urls import path
from .views import *

urlpatterns = [
 	path('list/user/', ListUsers.as_view(), name='visualize_users'),
 	path('register/user/', registerUser.as_view(), name='register_users'),
 	path('register/assign/', registerAssign.as_view(), name='assign_users'),



]