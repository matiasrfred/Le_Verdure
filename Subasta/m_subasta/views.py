from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from .serializers import *
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

def eliminar_subasta(id_subasta):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_SUBASTAS',[id_subasta,salida])



######################################################################################
class subastaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            subastas=list(Subasta.objects.filter(id_subasta=id).values())
            if len(subastas)>0:
                subasta = subastas[0]
                datos = {'message' : "Succes" , 'subasta':subasta}
            else:
                datos={'message' : "Subasta no encontrada ..."}
            return JsonResponse(datos)
        else:
            subastas=list(Subasta.objects.values())
            if len(subastas)>0:
                datos={'message' : "Succes" , 'subastas':subastas}
            else:
                datos={'message' : "Subasta no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_subasta(id_subasta=jd['id_subastas'],fecha_publicacion=jd['fecha_publicacion'],
        fecha_termino_sub=jd['fecha_termino_sub'],cond_carga=jd['cond_carga'],
        cond_tamano=jd['cond_tamano'],cond_refrigeracion=jd['cond_refrigeracion'], valor_inicial=jd['valor_inicial'],
        ultima_puja=jd['ultima_puja'],ctdad_pujas=jd['ctdad_pujas'], pdv_id_pdv=jd['pdv_id_pdv'],
        estado_sub=jd['estado_sub'],cap_transporte_id_transporte=jd['cap_transporte_id_transporte'] )
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id_subasta):
        jd = json.loads(request.body)
        subastas = list(Subasta.objects.filter(id_subasta=id_subasta).values())
        if len(subastas) > 0:
            modificar_subasta(id_subasta=jd['id_subasta'],fecha_publicacion=jd['fecha_publicacion'],
            fecha_termino_sub=jd['fecha_termino_sub'],cond_carga=jd['cond_carga'],
            cond_tamano=jd['cond_tamano'],cond_refrigeracion=jd['cond_refrigeracion'], valor_inicial=jd['valor_inicial'],
            ultima_puja=jd['ultima_puja'],ctdad_pujas=jd['ctdad_pujas'], pdv_id_pdv=jd['pdv_id_pdv'],
            estado_sub=jd['estado_sub'],cap_transporte_id_transporte=jd['cap_transporte_id_transporte'] )
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Subasta no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_subasta):
        jd = json.loads(request.body)
        subastas = list(Subasta.objects.filter(id_subasta=id_subasta).values())
        if len(subastas) > 0:
            eliminar_subasta(id_subasta=jd['id_subasta'])
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Subasta no encontrada ..."}
        return JsonResponse(datos)

class SubastaViewset(viewsets.ModelViewSet):
    queryset = Subasta.objects.filter()
    serializer_class = Subasta_srlzr


class SubastaAllViewset(viewsets.ModelViewSet):
    queryset = Subasta.objects.all()
    serializer_class = Subasta_allsrlzr

############################################################################################################################
