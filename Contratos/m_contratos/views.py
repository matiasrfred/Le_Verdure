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

def eliminar_contrato(id_contrato):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_CONTRATO',[id_contrato,salida])


class ContratoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_contrato=0):
        if (id_contrato>0):
            contratos=list(Contrato.objects.filter(id_contrato=id_contrato).values())
            if len(contratos)>0:
                contrato = contratos[0]
                datos = {'message' : "Exitoso" , 'contrato':contrato}
            else:
                datos={'message' : "Contrato no encontrado ..."}
            return JsonResponse(datos)
        else:
            contratos=list(Contrato.objects.values())
            if len(contratos)>0:
                datos={'message' : "Exitoso" , 'contratos':contratos}
            else:
                datos={'message' : "Contrato no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_contrato(fecha_inicio=jd['fecha_inicio'],fecha_termino=jd['fecha_termino'],contrato_activo=jd['contrato_activo'],usuario_id_usuario=jd['usuario_id_usuario'])
        datos={'message' : "Exitoso"}
        return JsonResponse(datos)

    def put(self,request, id_contrato):
        jd = json.loads(request.body)
        contratos = list(Contrato.objects.filter(id_contrato=id_contrato).values())
        if len(contratos) > 0:
            modificar_contrato(fecha_inicio=jd['fecha_inicio'],fecha_termino=jd['fecha_termino'],contrato_activo=jd['contrato_activo'],usuario_id_usuario=jd['usuario_id_usuario'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Contrato no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_contrato):
        jd = json.loads(request.body)
        contratos = list(Contrato.objects.filter(id_contrato=id_contrato).values())
        if len(contratos) > 0:
            eliminar_contrato(id_contrato=id_contrato)
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Contrato no encontrado ..."}
        return JsonResponse(datos)

class ContratoViewset(viewsets.ModelViewSet):
    queryset = Contrato.objects.filter(contrato_activo='1')
    serializer_class = Contrato_srlzr


class ContratoAllViewset(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = Contrato_allsrlzr