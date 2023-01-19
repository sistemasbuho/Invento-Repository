"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actives/',include(('apps.actives.urls','actives'))),
    path('users/', include(('apps.assignment.urls','users'))),        
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
    
	#path('', ViewHome, name='home'),

]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)



	# import debug_toolbar
	# urlpatterns = [
	# 	path('__debug__/', include(debug_toolbar.urls)),
	#] + urlpatterns    

admin.site.site_header = "Administrador de Invento"
admin.site.site_title = "Administración de Invento"
admin.site.index_title = "Administración de Invento"
