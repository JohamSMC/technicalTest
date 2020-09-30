from rest_framework.response import Response
from .serializers import DataSerializer
from rest_framework.views import APIView
from rest_framework import status

class DataApi(APIView):
    def get(self, request, inicio, final, paso):
        start = inicio
        end = final
        step = paso
        print(start)
        print(end)
        print(step)

        
        return Response("OK")