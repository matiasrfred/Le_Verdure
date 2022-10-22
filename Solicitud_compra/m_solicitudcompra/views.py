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

def eliminar_solicitud(email):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_SOLICITUD_COMPRA',[email,salida])