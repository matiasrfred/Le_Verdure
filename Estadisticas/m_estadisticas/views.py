from .models import *
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

class estadisticaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            estadisticass=list(Estadisticas.objects.filter(id_estad=id).values())
            if len(estadisticass)>0:
                estadistica = estadisticass[0]
                datos = {'message' : "Succes" , 'estadisticass':estadisticass}
            else:
                datos={'message' : "Estadistica de compra no encontrada ..."}
            return JsonResponse(datos)
        else:
            estadisticass=list(Estadisticas.objects.values())
            if len(estadisticass)>0:
                datos={'message' : "Succes" , 'estadisticass':estadisticass}
            else:
                datos={'message' : "Estadistica de compra no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        Estadisticas.objects.create(id_estad=jd['id_estad'],subasta_id_subasta_id=jd['subasta_id_subasta_id'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        estadisticass = list(Estadisticas.objects.filter(id_estad=id).values())
        if len(estadisticass) > 0:
            estadisticass=Estadisticas.objects.get(id_estad=id)
            estadisticass.id_estad=jd['id_estad']
            estadisticass.subasta_id_subasta_id=jd['subasta_id_subasta_id']
            estadisticass.save()
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Estadistica de compra no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id):
        estadisticass = list(Estadisticas.objects.filter(id_estad=id).values())
        if len(estadisticass) > 0:
            Estadisticas.objects.filter(id_estad=id).delete()
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Estadistica de compra no encontrada ..."}
        return JsonResponse(datos)

