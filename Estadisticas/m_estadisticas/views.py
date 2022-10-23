from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import cx_Oracle
from rest_framework import viewsets
from .serializers import *


##########################################
######### PROCESOS ALMACENADOS ###########
##########################################

def agregar_estadistica(id_estad,subasta_id_subasta_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_ESTADISTICAS',[id_estad,subasta_id_subasta_id,salida])
    return salida

def lista_estadistica():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_ESTADISTICAS', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_estadistica(id_estad,subasta_id_subasta_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_ESTADISTICAS',[id_estad,subasta_id_subasta_id,salida])

def eliminar_estadistica(id_estad):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_SUBASTAS',[id_estad,salida])

##########################################
############### CLASES VIEWSET ###########
##########################################
class estadisticaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_estad=0):
        if (id_estad>0):
            estadisticass=list(Estadisticas.objects.filter(id_estad=id_estad).values())
            if len(estadisticass)>0:
                estadistica = estadisticass[0]
                datos = {'message' : "Succes" , 'estadisticass':estadistica}
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
        agregar_estadistica(id_estad=jd['id_estad'],subasta_id_subasta_id=jd['subasta_id_subasta_id'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id_estad):
        jd = json.loads(request.body)
        estadisticass = list(Estadisticas.objects.filter(id_estad=id_estad).values())
        if len(estadisticass) > 0:
            modificar_estadistica(id_estad=jd['id_estad'],subasta_id_subasta_id=jd['subasta_id_subasta_id'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Estadistica de compra no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_estad):
        jd = json.loads(request.body)
        estadisticass = list(Subasta.objects.filter(id_estad=id_estad).values())
        if len(estadisticass) > 0:
            eliminar_estadistica(id_estad=jd['id_estad'])
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Estadistica de compra no encontrada ..."}
        return JsonResponse(datos)

class EstadisticasViewset(viewsets.ModelViewSet):
    queryset = Estadisticas.objects.filter()
    serializer_class = Estadisticas_srlzr


class EstadisticasAllViewset(viewsets.ModelViewSet):
    queryset = Estadisticas.objects.all()
    serializer_class = Estadisticas_allsrlzr