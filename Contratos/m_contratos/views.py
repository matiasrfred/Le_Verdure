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

def agregar_contrato(fecha_inicio,fecha_termino,contrato_activo,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    contrato_activo = '1'
    cursor.callproc('AGREGAR_CONTRATO',[fecha_inicio,fecha_termino,contrato_activo,usuario_id_usuario,salida])
    return salida

def lista_contrato():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_CONTRATO', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_contrato(fecha_inicio,fecha_termino,contrato_activo,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_CONTRATO',[fecha_inicio,fecha_termino,contrato_activo,usuario_id_usuario,salida])

def eliminar_contrato(email):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_CONTRATO',[email,salida])