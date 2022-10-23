from Usuarios.m_usuario.views import agregar_estado
from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import cx_Oracle
import json


# Create your views here.
##################Solicitud######################################################################################
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

def eliminar_solicitud(id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_SOLICITUD_COMPRA',[id_solicitud,salida])

####################################################################
#################        PRODUCTO          #########################
####################################################################

def agregar_producto(d_estado,ruta_imagen,calidad_id_calidad):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_PRODUCTO',[d_estado,ruta_imagen,calidad_id_calidad])
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
    cursor.callproc('ACTUALIZAR_PRODUCTO',[d_estado,ruta_imagen,calidad_id_calidad,salida])

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

class solicitudView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            solicitudes=list(SolicitudCompra.objects.filter(id_solicitud=id).values())
            if len(solicitudes)>0:
                solicitud = solicitudes[0]
                datos = {'message' : "Succes" , 'solicitudes':solicitudes}
            else:
                datos={'message' : "Solicitud de compra no encontrada ..."}
            return JsonResponse(datos)
        else:
            solicitudes=list(SolicitudCompra.objects.values())
            if len(solicitudes)>0:
                datos={'message' : "Succes" , 'solicitudes':solicitudes}
            else:
                datos={'message' : "Solicitud de compra no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_solicitud(id_solicitud=jd['id_solicitud'],fecha_solicitud=jd['fecha_solicitud'],
        ctdad_necesaria=jd['ctdad_necesaria'],estado_solicitud_id_estado_id=jd['estado_solicitud_id_estado_id'],
        producto_id_prod_id=jd['producto_id_prod_id'],usuario_id_usuario_id=jd['usuario_id_usuario_id'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        solicitudes = list(SolicitudCompra.objects.filter(id_solicitud=id).values())
        if len(solicitudes) > 0:
            modificar_solicitud(id_solicitud=jd['id_solicitud'],fecha_solicitud=jd['fecha_solicitud'],
            ctdad_necesaria=jd['ctdad_necesaria'],estado_solicitud_id_estado_id=jd['estado_solicitud_id_estado_id'],
            producto_id_prod_id=jd['producto_id_prod_id'],usuario_id_usuario_id=jd['usuario_id_usuario_id'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Solicitud de compra no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_solicitud):
        jd = json.loads(request.body)
        solicitud = list(SolicitudCompra.objects.filter(id_solicitud=id_solicitud).values())
        if len(solicitud) > 0:
            eliminar_solicitud(id_solicitud=id_solicitud)
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Solicitud de compra no encontrada ..."}
        return JsonResponse(datos)


###############################################
############## View EstadoSolicitud ###########
###############################################


class productoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            productos=list(EstadoSolicitud.objects.filter(id_estado=id).values())
            if len(productos)>0:
                producto = productos[0]
                datos = {'message' : "Succes" , 'productos':productos}
            else:
                datos={'message' : "EstadoSolicitud no encontrado ..."}
            return JsonResponse(datos)
        else:
            productos=list(EstadoSolicitud.objects.values())
            if len(productos)>0:
                datos={'message' : "Succes" , 'productos':productos}
            else:
                datos={'message' : "EstadoSolicitud no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_producto(id_estado=jd['id_estado'],d_estado=jd['d_estado'],
        ruta_imagen=jd['ruta_imagen'],calidad_id_calidad=jd['calidad_id_calidad'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        productos = list(EstadoSolicitud.objects.filter(id_estado=id).values())
        if len(productos) > 0:
            modificar_solicitud(id_estado=jd['id_estado'],d_estado=jd['d_estado'],
        ruta_imagen=jd['ruta_imagen'],calidad_id_calidad=jd['calidad_id_calidad'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "EstadoSolicitud no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_estado):
        jd = json.loads(request.body)
        solicitud = list(SolicitudCompra.objects.filter(id_estado=id_estado).values())
        if len(solicitud) > 0:
            eliminar_producto(id_estado=id_estado)
            datos={'message' : "Succes"}
        else:
            datos={'message' : "EstadoSolicitud no encontrado ..."}
        return JsonResponse(datos)

###############################################
############## View Calidad ###################
###############################################


class calidadView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            estadosolicitudes=list(Calidad.objects.filter(id_calidad=id).values())
            if len(estadosolicitudes)>0:
                calidad = estadosolicitudes[0]
                datos = {'message' : "Succes" , 'estadosolicitudes':estadosolicitudes}
            else:
                datos={'message' : "Calidad no encontrada ..."}
            return JsonResponse(datos)
        else:
            productos=list(EstadoSolicitud.objects.values())
            if len(estadosolicitudes)>0:
                datos={'message' : "Succes" , 'productos':productos}
            else:
                datos={'message' : "EstadoSolicitud no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_producto(id_estado=jd['id_estado'],d_estado=jd['d_estado'],
        ruta_imagen=jd['ruta_imagen'],calidad_id_calidad=jd['calidad_id_calidad'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        productos = list(EstadoSolicitud.objects.filter(id_estado=id).values())
        if len(productos) > 0:
            modificar_producto(id_estado=jd['id_estado'],d_estado=jd['d_estado'],
        ruta_imagen=jd['ruta_imagen'],calidad_id_calidad=jd['calidad_id_calidad'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "EstadoSolicitud no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_estado):
        jd = json.loads(request.body)
        producto = list(EstadoSolicitud.objects.filter(id_estado=id_estado).values())
        if len(producto) > 0:
            eliminar_producto(id_estado=id_estado)
            datos={'message' : "Succes"}
        else:
            datos={'message' : "EstadoSolicitud no encontrado ..."}
        return JsonResponse(datos)


###############################################
############## View Estado solicitud ##########
###############################################


class estadoSolicitudView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            estadosolicitudes=list(EstadoSolicitud.objects.filter(id_estado=id).values())
            if len(estadosolicitudes)>0:
                estadosolicitud = estadosolicitudes[0]
                datos = {'message' : "Succes" , 'estadosolicitudes':estadosolicitudes}
            else:
                datos={'message' : "Estado solicit no encontrada ..."}
            return JsonResponse(datos)
        else:
            estadosolicitudes=list(EstadoSolicitud.objects.values())
            if len(estadosolicitudes)>0:
                datos={'message' : "Succes" , 'estadosolicitudes':estadosolicitudes}
            else:
                datos={'message' : "Estado solicut no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_estado_solicitud(id_estado=jd['id_estado'],d_estado=jd['d_estado'])
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        estadosolicitudes = list(EstadoSolicitud.objects.filter(id_estado=id).values())
        if len(estadosolicitudes) > 0:
            modificar_estado_solicitud(id_estado=jd['id_estado'],d_estado=jd['d_estado'])
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "EstadoSolicitud no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_estado):
        jd = json.loads(request.body)
        estadosolicitud = list(EstadoSolicitud.objects.filter(id_estado=id_estado).values())
        if len(estadosolicitud) > 0:
            eliminar_estado_solicitud(id_estado=id_estado)
            datos={'message' : "Succes"}
        else:
            datos={'message' : "EstadoSolicitud no encontrado ..."}
        return JsonResponse(datos)