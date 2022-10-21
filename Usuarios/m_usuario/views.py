from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from .serializers import Usuario_srlzr,Usuario_allsrlzr
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import cx_Oracle
import datetime

# Create your views here.

def agregar_usuario(nombre,apellido,email,password,run,usuario_activo,superuser,ciudad_id_ciudad,rol_id_rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    usuario_activo = '1'
    cursor.callproc('AGREGAR_USER',[nombre,apellido,email,password,run,usuario_activo,superuser,ciudad_id_ciudad,rol_id_rol,salida])
    return salida

def lista_usuario():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_USER', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_usuario(nombre,apellido,email,password,run,usuario_activo,superuser,ciudad_id_ciudad,rol_id_rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_USER',[nombre,apellido,email,password,run,usuario_activo,superuser,ciudad_id_ciudad,rol_id_rol,salida])

def eliminar_usuario(email):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_USER',[email,salida])