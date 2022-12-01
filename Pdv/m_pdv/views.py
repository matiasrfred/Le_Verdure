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

###########################################################
################     Pdv    ###############################    
###########################################################


def agregar_pdv(fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_PDV',[fecha_comienzo,fecha_termino,ctdad_reunida,precio_total,estado_pdv_id_estadopdv,solicitud_compra_id_solicitud,tipo_local])
    return salida

def lista_pdv():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_PDV', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_pdv(id_pdv,ctdad_reunida,precio_total):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_PDV2',[id_pdv,ctdad_reunida,precio_total])
    return salida

def eliminar_pdv(id_pdv):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_PDV',[id_pdv,salida])

###########################################################
################     Estado Pdv    ########################    
###########################################################

def agregar_estadopdv(d_estadopdv):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_ESTADOPDV',[d_estadopdv])
    return salida

def lista_estadopdv():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_ESTADOPDV', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_estadopdv(d_estadopdv):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_ESTADOPDV',[d_estadopdv])

def eliminar_estadopdv(id_estadopdv):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_ESTADOPDV',[id_estadopdv,salida])

###########################################################
################     Ofertantes    ########################    
###########################################################

def agregar_ofertantes(precio_oferta,ctdad_ofertada,seleccion,pdv_id_pdv,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_OFERTANTES',[precio_oferta,ctdad_ofertada,seleccion,pdv_id_pdv,usuario_id_usuario])
    return salida

def lista_ofertantes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_OFERTANTES', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_ofertantes(precio_oferta,ctdad_ofertada,seleccion,pdv_id_pdv,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_OFERTANTES',[precio_oferta,ctdad_ofertada,seleccion,pdv_id_pdv,usuario_id_usuario])

def eliminar_ofertantes(id_oferta):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_OFERTANTES',[id_oferta,salida])



############################################################
################ View  Pdv #################################
############################################################

class pdvView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_pdv=0):
        if (id_pdv > 0):
            pdvs=list(Pdv.objects.filter(id_pdv=id_pdv).values())
            if len(pdvs)>0:
                pdv = pdvs[0]
                datos = {'message' : "Succes" , 'pdv':pdv}
            else:
                datos={'message' : "Proceso de venta no encontrado ..."}
            return JsonResponse(datos)
        else:
            pdvs = list(Pdv.objects.values())
            if len(pdvs) > 0:
                datos={'message' : "Succes" , 'pdvs':pdvs}
            else:
                datos={'message' : "Proceso de venta no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        try:
            jd = json.loads(request.body)
            try:
                agregar_pdv(fecha_comienzo=jd['fecha_comienzo'],
                fecha_termino=jd['fecha_termino'],
                ctdad_reunida=jd['ctdad_reunida'],
                precio_total=jd['precio_total'],
                estado_pdv_id_estadopdv=jd['estado_pdv_id_estadopdv_id'],
                solicitud_compra_id_solicitud=jd['solicitud_compra_id_solicitud_id'],
                tipo_local=jd['tipo_local'])
                datos={'message' : "Succes"}
                return JsonResponse(datos)
            except:
                return JsonResponse({'message': "No fue posible Agregar"},status=404)
        except:
            return JsonResponse({'message': "Validar Formato Json"},status=500)

    def put(self,request, id_pdv):
        jd = json.loads(request.body)
        pdvs = list(Pdv.objects.filter(id_pdv=id_pdv).values())
        if len(pdvs) > 0:
            modificar_pdv(id_pdv,
            ctdad_reunida=jd['ctdad_reunida'],
            precio_total=jd['precio_total'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Pdv no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_pdv):
        jd = json.loads(request.body)
        pdvs = list(Pdv.objects.filter(id_pdv=id_pdv).values())
        if len(pdvs) > 0:
            eliminar_pdv(id_pdv=jd['id_pdv'])
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Pdv no encontrada ..."}
        return JsonResponse(datos)

class PdvViewset(viewsets.ModelViewSet):
    queryset = Pdv.objects.all()
    serializer_class = Pdv_srlzr


class PdvAllViewset(viewsets.ModelViewSet):
    queryset = Pdv.objects.all()
    serializer_class = Pdv_allsrlzr


############################################################
################ View Estado Pdv ###########################
############################################################

class estadopdvView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_estadopdv=0):
        if (id_estadopdv>0):
            estadopdvs=list(EstadoPdv.objects.filter(id_estadopdv=id_estadopdv).values())
            if len(estadopdvs)>0:
                estadopdv = estadopdvs[0]
                datos = {'message' : "Success" , 'estadopdv':estadopdv}
            else:
                datos={'message' : "Estado del proceso de venta no encontrada ..."}
            return JsonResponse(datos)
        else:
            estadopdvs=list(EstadoPdv.objects.values())
            if len(estadopdvs)>0:
                datos={'message' : "Succes" , 'estadopdvs':estadopdvs}
            else:
                datos={'message' : "Estado del proceso de venta no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_estadopdv(id_estadopdv=jd['id_estadopdv'],d_estadopdv=jd['d_estadopdv'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id_estadopdv):
        jd = json.loads(request.body)
        estadopdvs = list(EstadoPdv.objects.filter(id_estadopdv=id_estadopdv).values())
        if len(estadopdvs) > 0:
            modificar_estadopdv(id_estadopdv=jd['id_estadopdv'],d_estadopdv=jd['d_estadopdv'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Estado del proceso de venta no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_estadopdv):
        jd = json.loads(request.body)
        estadopdvs = list(EstadoPdv.objects.filter(id_estadopdv=id_estadopdv).values())
        if len(estadopdvs) > 0:
            eliminar_estadopdv(id_estadopdv=jd['id_estadopdv'])
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Estado del proceso de venta no encontrada ..."}
        return JsonResponse(datos)

class EstadopdvViewset(viewsets.ModelViewSet):
    queryset = EstadoPdv.objects.all()
    serializer_class = EstadoPdv_srlzr


class EstadopdvAllViewset(viewsets.ModelViewSet):
    queryset = EstadoPdv.objects.all()
    serializer_class = EstadoPdv_allsrlzr


############################################################
################ View Ofertantes ###########################
############################################################


class ofertanteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            ofertantes=list(ofertante.objects.filter(id_oferta=id).values())
            if len(ofertantes)>0:
                ofertante = ofertantes[0]
                datos = {'message' : "Succes" , 'ofertantes':ofertantes}
            else:
                datos={'message' : "Ofertante no encontrado ..."}
            return JsonResponse(datos)
        else:
            ofertantes=list(Ofertantes.objects.values())
            if len(ofertantes)>0:
                datos={'message' : "Succes" , 'ofertantes':ofertantes}
            else:
                datos={'message' : "Ofertante no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_ofertantes(id_oferta=jd['id_oferta'],precio_oferta=jd['precio_oferta'],ctdad_ofertada=jd['ctdad_ofertada'],
        seleccion=jd['seleccion'],pdv_id_pdv=jd['pdv_id_pdv'],usuario_id_usuario=jd['usuario_id_usuario'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        ofertantes = list(Ofertantes.objects.filter(id_oferta=id).values())
        if len(ofertantes) > 0:
            modificar_ofertantes(id_oferta=jd['id_oferta'],precio_oferta=jd['precio_oferta'],ctdad_ofertada=jd['ctdad_ofertada'],
        seleccion=jd['seleccion'],pdv_id_pdv=jd['pdv_id_pdv'],usuario_id_usuario=jd['usuario_id_usuario'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Ofertante no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_oferta):
        jd = json.loads(request.body)
        ofertantes = list(Ofertantes.objects.filter(id_oferta=id_oferta).values())
        if len(ofertantes) > 0:
            eliminar_ofertantes(id_oferta=jd['id_oferta'])
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Ofertante no encontrado ..."}
        return JsonResponse(datos)

class OfertanteViewset(viewsets.ModelViewSet):
    queryset = Ofertantes.objects.filter()
    serializer_class = Ofertante_srlzr


class OfertanteAllViewset(viewsets.ModelViewSet):
    queryset = Ofertantes.objects.all()
    serializer_class = Ofertante_allsrlzr


