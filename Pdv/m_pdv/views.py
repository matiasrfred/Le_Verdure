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

def agregar_solicitud(fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_PDV',[fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local,salida])
    return salida

def lista_solicitud():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_PDV', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_solicitud(fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_PDV',[fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local,salida])

def eliminar_solicitud(email):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_PDV',[email,salida])


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
            pdvs=list(Subasta.objects.values())
            if len(pdvs)>0:
                datos={'message' : "Succes" , 'pdvs':pdvs}
            else:
                datos={'message' : "Proceso de venta no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        Pdv.objects.create(id_pdv=jd['id_pdv'], fecha_comienzo=jd[' fecha_comienzo'],fecha_termino=jd['fecha_termino'],ctdad_reunida=jd['ctdad_reunida'],precio_total=jd['precio_total'],estado_pdv_id_estadopdv=jd['estado_pdv_id_estadopdv'],solicitud_compra_id_solicitud=jd['solicitud_compra_id_solicitud'],tipo_local=jd['tipo_local'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        pdvs = list(Subasta.objects.filter(id_pdv=id).values())
        if len(pdvs) > 0:
            pdv=Pdv.objects.get(id_pdv=id)
            pdv.id_pdv=jd['id_pdv']
            pdv.fecha_comienzo=jd['fecha_comienzo']
            pdv.fecha_termino=jd['fecha_termino']
            pdv.ctdad_reunida=jd['ctdad_reunida']
            pdv.precio_total=jd['precio_total']
            pdv.estado_pdv_id_estadopdv=jd['estado_pdv_id_estadopdv']
            pdv.solicitud_compra_id_solicitud=jd['solicitud_compra_id_solicitud']
            pdv.tipo_local=jd['tipo_local']
            pdv.save()
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Pdv no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id):
        pdvs = list(Pdv.objects.filter(id_pdv=id).values())
        if len(pdvs) > 0:
            Pdv.objects.filter(id_pdv=id).delete()
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Pdv no encontrada ..."}
        return JsonResponse(datos)