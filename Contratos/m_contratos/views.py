from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from .serializers import Contrato_srlzr,Contrato_allsrlzr
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import cx_Oracle
import datetime

# Create your views here.



class contratoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            contratos=list(Contrato.objects.filter(id_contrato=id).values())
            if len(contratos)>0:
                contrato = contratos[0]
                datos = {'message' : "Succes" , 'contrato':contrato}
            else:
                datos={'message' : "Contrato no encontrado ..."}
            return JsonResponse(datos)
        else:
            contratos=list(Contrato.objects.values())
            if len(contratos)>0:
                datos={'message' : "Succes" , 'contratos':contratos}
            else:
                datos={'message' : "Contrato no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        Contrato.objects.create(id_contrato=jd['id_contrato'], fecha_inicio=jd['fecha_inicio'], fecha_termino=jd ['fecha_termino'], contrato_activo=jd ['contrato_activo'], usuario_id_usuario=jd ['usuario_id_usuario'] )
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        contratos = list(Contrato.objects.filter(id_contrato=id).values())
        if len(contratos) > 0:
            contrato=Contrato.objects.get(id_contrato=id)
            contrato.id_contrato=jd['id_contrato']
            contrato.fecha_inicio=jd['fecha_inicio']
            contrato.fecha_termino=jd['fecha_termino']
            contrato.contrato_activo=jd['contrato_activo']
            contrato.usuario_id_usuario=jd['usuario_id_usuario']
            contrato.save()
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Contrato no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id):
        contratos = list(Contrato.objects.filter(id_contrato=id).values())
        if len(contratos) > 0:
            Contrato.objects.filter(id_contrato=id).delete()
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Contrato no encontrado ..."}
        return JsonResponse(datos)