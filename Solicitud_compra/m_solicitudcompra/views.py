import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework import viewsets
from .serializers import *
from django.http.response import JsonResponse
from django.db import connection
import cx_Oracle


# Create your views here.
##################Solicitud######################################################################################
def agregar_solicitud(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado,producto_id_prod,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_SOLICITUD_COMPRA',[fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado,producto_id_prod,usuario_id_usuario])
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




####################################################################
#################        PRODUCTO          #########################
####################################################################

def agregar_producto(n_prod,ruta_imagen,calidad_id_calidad,producto_activo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_PRODUCTO',[n_prod,ruta_imagen,calidad_id_calidad,producto_activo])
    return salida

def lista_producto():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_PRODUCTO', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_producto(d_estado,ruta_imagen,calidad_id_calidad):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_PRODUCTO',[d_estado,ruta_imagen,calidad_id_calidad])
    return salida

def eliminar_producto(id_estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_PRODUCTO',[id_estado,salida])

####################################################################
#################        Calidad          ##########################
####################################################################

def agregar_calidad(descripcion_c):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_CALIDAD',[descripcion_c])
    return salida

def lista_calidad():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_CALIDAD', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_calidad(descripcion_c):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_CALIDAD',[descripcion_c])

def eliminar_calidad(id_calidad):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_CALIDAD',[id_calidad,salida])

####################################################################
#################      Estado solicitud         ######################
####################################################################

def agregar_estado_solicitud(d_estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_ESTADO_SOLICITUD',[d_estado])
    return salida

def lista_estado_solicitud():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_ESTADO_SOLICITUD', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_estado_solicitud(d_estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_ESTADO_SOLICITUD',[d_estado])

def eliminar_estado_solicitud(id_estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_ESTADO_SOLICITUD',[id_estado,salida])





###############################################
########### View Solicitud Compra #############
###############################################

class SolicitudView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, requests, id_solicitud=0):
        if (id_solicitud>0):
            solicitudes=list(SolicitudCompra.objects.filter(id_solicitud=id_solicitud).values())
            if len(solicitudes)>0:
                solicitud = solicitudes[0]
                datos = {'message' : "Exitoso" , 'solicitud':solicitud}
            else:
                datos={'message' : "Solicitud de compra no encontrada ..."}
            return JsonResponse(datos)
        else:
            solicitudes=list(SolicitudCompra.objects.values())
            if len(solicitudes)>0:
                datos={'message' : "Exitoso" , 'solicitudes':solicitudes}
            else:
                datos={'message' : "Solicitud de compra no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_solicitud(fecha_solicitud=jd['fecha_solicitud'],
        ctdad_necesaria=jd['ctdad_necesaria'],
        estado_solicitud_id_estado=jd['estado_solicitud_id_estado_id'],
        producto_id_prod=jd['producto_id_prod_id'],
        usuario_id_usuario=jd['usuario_id_usuario_id'])
        datos={'message' : "Exitoso"}
        return JsonResponse(datos)

    def put(self,request, id_solicitud):
        jd = json.loads(request.body)
        solicitudes = list(SolicitudCompra.objects.filter(id_solicitud=id_solicitud).values())
        if len(solicitudes)>0:
            modificar_solicitud(id_solicitud=jd['id_solicitud'],fecha_solicitud=jd['fecha_solicitud'],ctdad_necesaria=jd['ctdad_necesaria'],estado_solicitud_id_estado_id=jd['estado_solicitud_id_estado_id'],producto_id_prod_id=jd['producto_id_prod_id'],usuario_id_usuario_id=jd['usuario_id_usuario_id'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Solicitud de compra no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_solicitud):
        jd = json.loads(request.body)
        solicitud = list(SolicitudCompra.objects.filter(id_solicitud=id_solicitud).values())
        if len(solicitud)>0:
            eliminar_solicitud(id_solicitud=jd['id_solicitud'])
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Solicitud de compra no encontrada ..."}
        return JsonResponse(datos)

class SolicitudViewset(viewsets.ModelViewSet):
    queryset = SolicitudCompra.objects.all()
    serializer_class = Solicitud_srlzr


class SolicitudAllViewset(viewsets.ModelViewSet):
    queryset = SolicitudCompra.objects.all()
    serializer_class = Solicitud_allsrlzr

###############################################
############## View Producto ##################
###############################################


class ProductoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_prod=0):
        if (id_prod>0):
            productos=list(Producto.objects.filter(id_prod=id_prod).values())
            if len(productos)>0:
                producto = productos[0]
                datos = {'message' : "Exitoso" , 'producto':producto}
            else:
                datos={'message' : "Producto no encontrado ..."}
            return JsonResponse(datos)
        else:
            productos=list(Producto.objects.values())
            if len(productos)>0:
                datos={'message' : "Exitoso" , 'productos':productos}
            else:
                datos={'message' : "Producto no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_producto(
        n_prod=jd['n_prod'],
        ruta_imagen=jd['ruta_imagen'],
        calidad_id_calidad=jd['calidad_id_calidad_id'],
        producto_activo=jd['producto_activo'])
        datos={'message' : "Exitoso"}
        return JsonResponse(datos)

    def put(self,request, id_prod):
        jd = json.loads(request.body)
        productos = list(Producto.objects.filter(id_prod=id_prod).values())
        if len(productos) > 0:
            modificar_producto(id_prod=jd['id_prod'],
            n_prod=jd['n_prod'],
            ruta_imagen=jd['ruta_imagen'],
            calidad_id_calidad=jd['calidad_id_calidad'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Producto no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_prod):
        jd = json.loads(request.body)
        producto = list(Producto.objects.filter(id_prod=id_prod).values())
        if len(producto) > 0:
            eliminar_producto(id_prod=id_prod)
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Producto no encontrado ..."}
        return JsonResponse(datos)

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.filter()
    serializer_class = Producto_srlzr


class ProductoAllViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_allsrlzr

###############################################
############## View Calidad ###################
###############################################


class CalidadView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_calidad=0):
        if (id_calidad>0):
            calidades=list(Calidad.objects.filter(id_calidad=id_calidad).values())
            if len(calidades)>0:
                calidad = calidades[0]
                datos = {'message' : "Exitoso" , 'calidad':calidad}
            else:
                datos={'message' : "Calidad no encontrada ..."}
            return JsonResponse(datos)
        else:
            calidades=list(Calidad.objects.values())
            if len(calidades)>0:
                datos={'message' : "Exitoso" , 'calidades':calidades}
            else:
                datos={'message' : "Calidades no encontradas ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_calidad(id_calidad=jd['id_calidad'],descripcion_c=jd['descripcion_c'])
        datos={'message' : "Exitoso"}
        return JsonResponse(datos)

    def put(self,request, id_calidad):
        jd = json.loads(request.body)
        calidades = list(Calidad.objects.filter(id_calidad=id_calidad).values())
        if len(calidades) > 0:
            modificar_calidad(id_calidad=jd['id_calidad'],descripcion_c=jd['descripcion_c'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Calidad no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_calidad):
        jd = json.loads(request.body)
        calidad = list(Calidad.objects.filter(id_calidad=id_calidad).values())
        if len(calidad) > 0:
            eliminar_calidad(id_calidad=jd['id_calidad'])
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Calidad no encontrado ..."}
        return JsonResponse(datos)

class CalidadViewset(viewsets.ModelViewSet):
    queryset = Calidad.objects.filter()
    serializer_class = Calidad_srlzr


class CalidadAllViewset(viewsets.ModelViewSet):
    queryset = Calidad.objects.all()
    serializer_class = Calidad_allsrlzr

###############################################
############## View Estado solicitud ##########
###############################################


class estadoSolicitudView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_estado=0):
        if (id_estado>0):
            estadosolicitudes=list(EstadoSolicitud.objects.filter(id_estado=id_estado).values())
            if len(estadosolicitudes)>0:
                estadosolicitud = estadosolicitudes[0]
                datos = {'message' : "Exitoso" , 'estadosolicitud':estadosolicitud}
            else:
                datos={'message' : "Estado solicit no encontrada ..."}
            return JsonResponse(datos)
        else:
            estadosolicitudes=list(EstadoSolicitud.objects.values())
            if len(estadosolicitudes)>0:
                datos={'message' : "Exitoso" , 'estadosolicitudes':estadosolicitudes}
            else:
                datos={'message' : "Estado solicut no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_estado_solicitud(id_estado=jd['id_estado'],d_estado=jd['d_estado'])
        datos={'message' : "Exitoso"}
        return JsonResponse(datos)

    def put(self,request, id_estado):
        jd = json.loads(request.body)
        estadosolicitudes = list(EstadoSolicitud.objects.filter(id_estado=id_estado).values())
        if len(estadosolicitudes) > 0:
            modificar_estado_solicitud(id_estado=jd['id_estado'],d_estado=jd['d_estado'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "EstadoSolicitud no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_estado):
        jd = json.loads(request.body)
        estadosolicitud = list(EstadoSolicitud.objects.filter(id_estado=id_estado).values())
        if len(estadosolicitud) > 0:
            eliminar_estado_solicitud(id_estado=jd['id_estado'])
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "EstadoSolicitud no encontrado ..."}
        return JsonResponse(datos)

class EstadoSolicitudViewset(viewsets.ModelViewSet):
    queryset = EstadoSolicitud.objects.all()
    serializer_class = estadoSolicitud_srlzr


class EstadoSolicitudAllViewset(viewsets.ModelViewSet):
    queryset = EstadoSolicitud.objects.all()
    serializer_class = estadoSolicitud_allsrlzr