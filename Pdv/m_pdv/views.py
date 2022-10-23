from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from .serializers import Pdv_srlzr,Pdv_allsrlzr
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import cx_Oracle
import datetime
# Create your views here.


def agregar_pdv(fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_PDV',[fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local])
    return salida

def lista_pdv():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_PDV', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_pdv(fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_PDV',[fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local])

def eliminar_pdv(id_pdv):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_PDV',[id_pdv,salida])


###########################################################

class pdvView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            pdvs=list(pdv.objects.filter(id_pdv=id).values())
            if len(pdvs)>0:
                pdv = pdvs[0]
                datos = {'message' : "Succes" , 'pdv':pdv}
            else:
                datos={'message' : "Proceso de venta no encontrada ..."}
            return JsonResponse(datos)
        else:
            pdvs=list(Pdv.objects.values())
            if len(pdvs)>0:
                datos={'message' : "Succes" , 'pdvs':pdvs}
            else:
                datos={'message' : "Proceso de venta no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_pdv(id_pdv=jd['id_pdv'], fecha_comienzo=jd[' fecha_comienzo'],fecha_termino=jd['fecha_termino'],
        ctdad_reunida=jd['ctdad_reunida'],precio_total=jd['precio_total'],estado_pdv_id_estadopdv=jd['estado_pdv_id_estadopdv'],
        solicitud_compra_id_solicitud=jd['solicitud_compra_id_solicitud'],tipo_local=jd['tipo_local'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        pdvs = list(Pdv.objects.filter(id_pdv=id).values())
        if len(pdvs) > 0:
            modificar_pdv(id_pdv=jd['id_pdv'], fecha_comienzo=jd[' fecha_comienzo'],fecha_termino=jd['fecha_termino'],
            ctdad_reunida=jd['ctdad_reunida'],precio_total=jd['precio_total'],estado_pdv_id_estadopdv=jd['estado_pdv_id_estadopdv'],
            solicitud_compra_id_solicitud=jd['solicitud_compra_id_solicitud'],tipo_local=jd['tipo_local'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Pdv no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_pdv):
        pdvs = list(Pdv.objects.filter(id_pdv=id_pdv).values())
        if len(pdvs) > 0:
            eliminar_pdv(id_pdv=id_pdv)
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Pdv no encontrada ..."}
        return JsonResponse(datos)