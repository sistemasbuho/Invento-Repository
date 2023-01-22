from http.client import HTTPResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse
from django.views.generic import View,CreateView
from apps.actives.models import PassiveDevices

class SearchPassiveDevices(PermissionRequiredMixin,View):
	model = PassiveDevices
	permission_required = 'assignment.add_assignment'
	#http://127.0.0.1:8000/users/search/search_passive_devices/?term=test&_type=query&q=test
 
	def get(self, request, *args, **kwargs):
		try:
			data = request.GET.dict()
			print('data',data)
			default_state = data['state'] if 'state' in data else "Activo disponible"
			print("default_state ",default_state)
			data_dict_result = []
			query = self.model.objects.filter(state=default_state).values('id', 'name')

			if 'term' in data:
				#http://127.0.0.1:8000/users/search/search_passive_devices/?term=Activo&state=Activo%20disponible
				query = self.model.objects.filter(
					state=data['state'],
					name__icontains=data['term'].strip()
				).values('id', 'name')
				
			for i in query:
				data_list = {
					'id': i['id'],
					'name': i['name']
				}
				data_dict_result.append(data_list)            
			return JsonResponse(data_dict_result, safe=False)
		except Exception as Error:
			return HTTPResponse(f"Error del servidor de tipo: {str(Error)}")