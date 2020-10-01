from numpy.lib.npyio import load
from rest_framework.response import Response
from .serializers import DataSerializer
from rest_framework import status
from rest_framework.views import APIView
from .apiCalculations import ApiCalculations
from django.http import JsonResponse
class DataApi(APIView):

	def get(self, request, inicio, final, paso):
		start = inicio
		end = final
		step = paso
		outputs = ApiCalculations.executeCalculations(self, start,end,step)

		return JsonResponse(outputs, safe=False)
		#return Response(outpus)
