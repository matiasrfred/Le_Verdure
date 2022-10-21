from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from .serializers import Solicitud_srlzr,SolicitudSolicitud_allsrlzr
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