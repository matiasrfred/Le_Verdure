from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from .serializers import Subasta_srlzr,Subasta_allsrlzr
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import cx_Oracle
import datetime

# Create your views here.

def agregar_subasta(fecha_publicacion,fecha_termino_sub,cond_carga,cond_tamano,cond_refrigeracion,valor_inicial,ultima_puja,ctdad_pujas,pdv_id_pdv,estado_sub,cap_transporte_id_transporte):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    estado_sub = '1'
    cursor.callproc('AGREGAR_SUBASTAS',[fecha_publicacion,fecha_termino_sub,cond_carga,cond_tamano,cond_refrigeracion,valor_inicial,ultima_puja,ctdad_pujas,pdv_id_pdv,estado_sub,cap_transporte_id_transporte,salida])
    return salida

def lista_subasta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_SUBASTAS', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_subasta(fecha_publicacion,fecha_termino_sub,cond_carga,cond_tamano,cond_refrigeracion,valor_inicial,ultima_puja,ctdad_pujas,pdv_id_pdv,estado_sub,cap_transporte_id_transporte):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_SUBASTAS',[fecha_publicacion,fecha_termino_sub,cond_carga,cond_tamano,cond_refrigeracion,valor_inicial,ultima_puja,ctdad_pujas,pdv_id_pdv,estado_sub,cap_transporte_id_transporte,salida])

def eliminar_subasta(email):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_SUBASTAS',[email,salida])