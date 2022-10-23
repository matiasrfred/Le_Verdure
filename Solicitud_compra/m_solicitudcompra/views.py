from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import cx_Oracle
import json


# Create your views here.

def agregar_solicitud(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado,producto_id_prod,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_SOLICITUD_COMPRA',[fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado,producto_id_prod,usuario_id_usuario,salida])
    return salida

def lista_solicitud():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_SOLICITUD_COMPRA', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_solicitud(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado,producto_id_prod,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_SOLICITUD_COMPRA',[fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado,producto_id_prod,usuario_id_usuario,salida])

def eliminar_solicitud(id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_SOLICITUD_COMPRA',[id_solicitud,salida])

###############################################
########### View Solicitud Compra #############
###############################################

class solicitudView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            solicitudes=list(SolicitudCompra.objects.filter(id_solicitud=id).values())
            if len(solicitudes)>0:
                solicitud = solicitudes[0]
                datos = {'message' : "Succes" , 'solicitudes':solicitudes}
            else:
                datos={'message' : "Solicitud de compra no encontrada ..."}
            return JsonResponse(datos)
        else:
            solicitudes=list(SolicitudCompra.objects.values())
            if len(solicitudes)>0:
                datos={'message' : "Succes" , 'solicitudes':solicitudes}
            else:
                datos={'message' : "Solicitud de compra no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_solicitud(id_solicitud=jd['id_solicitud'],fecha_solicitud=jd['fecha_solicitud'],
        ctdad_necesaria=jd['ctdad_necesaria'],estado_solicitud_id_estado_id=jd['estado_solicitud_id_estado_id'],
        producto_id_prod_id=jd['producto_id_prod_id'],usuario_id_usuario_id=jd['usuario_id_usuario_id'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        solicitudes = list(SolicitudCompra.objects.filter(id_solicitud=id).values())
        if len(solicitudes) > 0:
            modificar_solicitud(id_solicitud=jd['id_solicitud'],fecha_solicitud=jd['fecha_solicitud'],
            ctdad_necesaria=jd['ctdad_necesaria'],estado_solicitud_id_estado_id=jd['estado_solicitud_id_estado_id'],
            producto_id_prod_id=jd['producto_id_prod_id'],usuario_id_usuario_id=jd['usuario_id_usuario_id'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Solicitud de compra no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_solicitud):
        jd = json.loads(request.body)
        solicitud = list(SolicitudCompra.objects.filter(id_solicitud=id_solicitud).values())
        if len(solicitud) > 0:
            eliminar_solicitud(id_solicitud=id_solicitud)
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Solicitud de compra no encontrada ..."}
        return JsonResponse(datos)

