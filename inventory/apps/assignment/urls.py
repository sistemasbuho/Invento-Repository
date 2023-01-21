from django.urls import path
from .views import *

urlpatterns = [
 	path('list/user/', ListUsers.as_view(), name='visualize_users'),
 	path('register/user/', registerUser.as_view(), name='register_users'),
 	path('register/assign/', registerAssign.as_view(), name='assign_users'),
 	path('details/assign/<int:pk>', UserDetailView.as_view(), name='detail_users'),
 	path('update/assign/<int:pk>', UpdateAssigment.as_view(), name='update_assignment'),
 	path('generate/<int:pk>', GeneratePdf.as_view(), name='generate_pdf'),


]