import json
from unicodedata import name
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework import viewsets
from .serializers import *
from django.http.response import JsonResponse
from django.db import connection
import cx_Oracle



##############################################################################
##############################################################################
#                                                                            #
#                              DEF PROC. ALM.                                #
#                                                                            #
##############################################################################
##############################################################################



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

def eliminar_usuario(id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_USER',[id_usuario,salida])

###############################################################################

def agregar_pais(id_pais,n_pais):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_PAIS',[id_pais,n_pais,salida])
    return salida

def lista_pais():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_PAIS', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_pais(id_pais,n_pais):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_PAIS',[id_pais,n_pais,salida])

def eliminar_pais(id_pais):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_PAIS',[id_pais,salida])

###############################################################################

def agregar_estado(id_estado,n_estado,pais_id_pais):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_ESTADOS',[id_estado,n_estado,pais_id_pais,salida])
    return salida

def lista_estado():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_ESTADOS', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_estado(id_estado,n_estado,pais_id_pais):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_ESTADOS',[id_estado,n_estado,pais_id_pais,salida])

def eliminar_estado(id_estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_ESTADOS',[id_estado,salida])

#######################################

def agregar_ciudad(id_ciudad,n_ciudad,estados_id_estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_CIUDAD',[id_ciudad,n_ciudad,estados_id_estado,salida])
    return salida

def lista_ciudad():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_CIUDAD', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_ciudad(id_ciudad,n_ciudad,estados_id_estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_CIUDAD',[id_ciudad,n_ciudad,estados_id_estado,salida])

def eliminar_ciudad(id_ciudad):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_CIUDAD',[id_ciudad,salida])

###################################################################

def agregar_rol(id_rol,n_rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_ROL',[id_rol,n_rol,salida])
    return salida

def lista_rol():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_ROL', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_rol(id_rol,n_rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_ROL',[id_rol,n_rol,salida])

def eliminar_rol(id_rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_ROL',[id_rol,salida])

#######################################

def agregar_cap_transporte(id_transporte,refrigeracion,cap_carga,cap_tamano,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_CAP_TRANSPORTE',[id_transporte,refrigeracion,cap_carga,cap_tamano,usuario_id_usuario,salida])
    return salida

def lista_cap_transporte():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_salida = django_cursor.connection.cursor()
    cursor.callproc('LISTAR_CAP_TRANSPORTE', [cursor_salida])
    list = []
    for fila in cursor_salida:
        list.append(fila)
    return list

def modificar_cap_transporte(id_transporte,refrigeracion,cap_carga,cap_tamano,usuario_id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_CAP_TRANSPORTE',[id_transporte,refrigeracion,cap_carga,cap_tamano,usuario_id_usuario,salida])

def eliminar_cap_transporte(id_transporte):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_CAP_TRANSPORTE',[id_transporte,salida])



##############################################################################
##############################################################################
#                                                                            #
#                               CLASES VIEWS                                 #
#                                                                            #
##############################################################################
##############################################################################



class UsuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_usuario=0):
        if (id_usuario>0):
            usuarios=list(Usuario.objects.filter(id_usuario=id_usuario).values())
            if len(usuarios)>0:
                usuario = usuarios[0]
                datos = {'message' : "Exitoso" , 'usuario':usuario}
            else:
                datos={'message' : "Usuario no encontrado ..."}
            return JsonResponse(datos)
        else:
            usuarios=list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message' : "Exitoso" , 'usuarios':usuarios}
            else:
                datos={'message' : "Usuario no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_usuario(id_usuario=jd['id_usuario'],nombre=jd['nombre'],apellido=jd['apellido'],email=jd['email'],password=jd['password'],run=jd['run'],usuario_activo=jd['usuario_activo'],superuser=jd['superuser'],ciudad_id_ciudad_id=jd['ciudad_id_ciudad_id'], rol_id_rol_id=jd['rol_id_rol_id'])
        datos={'message' : "Exitoso"}
        return JsonResponse(datos)

    def put(self,request, id_usuario):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id_usuario=id_usuario).values())
        if len(usuarios) > 0:
            modificar_usuario(id_usuario=jd['id_usuario'],nombre=jd['nombre'],apellido=jd['apellido'],email=jd['email'],password=jd['password'],run=jd['run'],usuario_activo=jd['usuario_activo'],superuser=jd['superuser'],ciudad_id_ciudad_id=jd['ciudad_id_ciudad_id'], rol_id_rol_id=jd['rol_id_rol_id'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Usuario no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_usuario):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id_usuario=id_usuario).values())
        if len(usuarios) > 0:
            eliminar_usuario(id_usuario=id_usuario)
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Usuario no encontrado ..."}
        return JsonResponse(datos)

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(usuario_activo='1')
    serializer_class = Usuario_srlzr


class UsuarioAllViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_allsrlzr

###########################################################
class PaisView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_pais=0):
        if (id_pais>0):
            paises=list(Pais.objects.filter(id_pais=id_pais).values())
            if len(paises)>0:
                pais = paises[0]
                datos = {'message' : "Exitoso" , 'pais':pais}    
            else:
                datos={'message' : "Pais no encontrado ..."}
            return JsonResponse(datos)
        else:
            paises=list(Pais.objects.values())
            if len(paises)>0:
                datos={'message' : "Exitoso" , 'paises':paises}
            else:
                datos={'message' : "Pais no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_pais(id_pais=jd['id_pais'],n_pais=jd['n_pais'])
        datos={'message' : "Exitosos"}
        return JsonResponse(datos)

    def put(self,request, id_pais):
        jd = json.loads(request.body)
        paises = list(Pais.objects.filter(id_pais=id_pais).values())
        if len(paises) > 0:
            modificar_pais(id_pais=jd['id_pais'],n_pais=jd['n_pais'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Pais no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_pais):
        jd = json.loads(request.body)
        paises = list(Pais.objects.filter(id_pais=id_pais).values())
        if len(paises) > 0:
            eliminar_pais(id_pais=id_pais)
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Pais no encontrado ..."}
        return JsonResponse(datos)

class PaisViewset(viewsets.ModelViewSet):
    queryset = Pais.objects.filter()
    serializer_class = Pais_srlzr


class PaisAllViewset(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = Pais_allsrlzr

###########################################################
class EstadosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_estado=0):
        if (id_estado>0):
            estados=list(Estados.objects.filter(id_estado=id_estado).values())
            if len(estados)>0:
                estado = estados[0]
                datos = {'message' : "Exitoso" , 'estado':estado}    
            else:
                datos={'message' : "Estado no encontrado ..."}
            return JsonResponse(datos)
        else:
            estados=list(Estados.objects.values())
            if len(estados)>0:
                datos={'message' : "Exitoso" , 'estados':estados}
            else:
                datos={'message' : "Estado no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_estado(id_estado=jd['id_estado'],n_estado=jd['n_estado'],pais_id_pais=jd['pais_id_pais'])
        datos={'message' : "Exitosos"}
        return JsonResponse(datos)

    def put(self,request, id_estado):
        jd = json.loads(request.body)
        estados = list(Estados.objects.filter(id_estado=id_estado).values())
        if len(estados) > 0:
            modificar_estado(id_estado=jd['id_estado'],n_estado=jd['n_estado'],pais_id_pais=jd['pais_id_pais'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Estado no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_estado):
        jd = json.loads(request.body)
        estados = list(Estados.objects.filter(id_estado=id_estado).values())
        if len(estados) > 0:
            eliminar_estado(id_estado=id_estado)
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Estado no encontrado ..."}
        return JsonResponse(datos)

class EstadosViewset(viewsets.ModelViewSet):
    queryset = Estados.objects.filter()
    serializer_class = Estados_srlzr


class EstadosAllViewset(viewsets.ModelViewSet):
    queryset = Estados.objects.all()
    serializer_class = Estados_allsrlzr


###########################################################
class CiudadView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_ciudad=0):
        if (id_ciudad>0):
            ciudades=list(Ciudad.objects.filter(id_ciudad=id_ciudad).values())
            if len(ciudades)>0:
                ciudad = ciudades[0]
                datos = {'message' : "Exitoso" , 'ciudad':ciudad}    
            else:
                datos={'message' : "Ciudad no encontrada ..."}
            return JsonResponse(datos)
        else:
            ciudades=list(Ciudad.objects.values())
            if len(ciudades)>0:
                datos={'message' : "Exitoso" , 'ciudades':ciudades}
            else:
                datos={'message' : "Ciudades no encontradas ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_ciudad(id_ciudad=jd['id_ciudad'],n_ciudad=jd['n_ciudad'],estados_id_estado=jd['estados_id_estado'])
        datos={'message' : "Exitosos"}
        return JsonResponse(datos)

    def put(self,request, id_ciudad):
        jd = json.loads(request.body)
        ciudades = list(Ciudad.objects.filter(id_ciudad=id_ciudad).values())
        if len(ciudades) > 0:
            modificar_ciudad(id_ciudad=jd['id_ciudad'],n_ciudad=jd['n_ciudad'],estados_id_estado=jd['estados_id_estado'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Ciudad no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id_ciudad):
        jd = json.loads(request.body)
        ciudades = list(Ciudad.objects.filter(id_ciudad=id_ciudad).values())
        if len(ciudades) > 0:
            eliminar_ciudad(id_ciudad=id_ciudad)
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Ciudad no encontrado ..."}
        return JsonResponse(datos)

class CiudadViewset(viewsets.ModelViewSet):
    queryset = Ciudad.objects.filter()
    serializer_class = Ciudad_srlzr


class CiudadAllViewset(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = Ciudad_allsrlzr

 ###########################################################
class RolView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_rol=0):
        if (id_rol>0):
            roles=list(Rol.objects.filter(id_rol=id_rol).values())
            if len(roles)>0:
                rol = roles[0]
                datos = {'message' : "Exitoso" , 'rol':rol}    
            else:
                datos={'message' : "Rol no encontrado ..."}
            return JsonResponse(datos)
        else:
            roles=list(Rol.objects.values())
            if len(roles)>0:
                datos={'message' : "Exitoso" , 'roles':roles}
            else:
                datos={'message' : "Rol no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_rol(id_rol=jd['id_rol'],n_rol=jd['n_rol'])
        datos={'message' : "Exitosos"}
        return JsonResponse(datos)

    def put(self,request, id_rol):
        jd = json.loads(request.body)
        roles = list(Rol.objects.filter(id_rol=id_rol).values())
        if len(roles) > 0:
            modificar_rol(id_rol=jd['id_rol'],n_rol=jd['n_rol'])
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Rol no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_rol):
        jd = json.loads(request.body)
        roles = list(Rol.objects.filter(id_rol=id_rol).values())
        if len(roles) > 0:
            eliminar_rol(id_rol=id_rol)
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Rol no encontrado ..."}
        return JsonResponse(datos)       

class RolViewset(viewsets.ModelViewSet):
    queryset = Rol.objects.filter()
    serializer_class = Rol_srlzr


class RolAllViewset(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = Rol_allsrlzr

#########################################################################
class TransporteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id_transporte=0):
        if (id_transporte>0):
            Transportes=list(CapTransporte.objects.filter(id_transporte=id_transporte).values())
            if len(Transportes)>0:
                transporte = Transportes[0]
                datos = {'message' : "Exitoso" , 'transporte':transporte}
            else:
                datos={'message' : "Transporte no encontrado ..."}
            return JsonResponse(datos)
        else:
            Transportes=list(CapTransporte.objects.values())
            if len(Transportes)>0:
                datos={'message' : "Exitoso" , 'Transportes':Transportes}
            else:
                datos={'message' : "Transporte no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        agregar_cap_transporte(id_transporte=jd['id_transporte'],refrigeracion=jd['refrigeracion'],cap_carga=jd['cap_carga'],cap_tamano=jd['cap_tamano'],usuario_id_usuario=jd['usuario_id_usuario'])
        datos={'message' : "Exitoso"}
        return JsonResponse(datos)

    def put(self,request, id_transporte):
        jd = json.loads(request.body)
        Transportes = list(CapTransporte.objects.filter(id_transporte=id_transporte).values())
        if len(Transportes) > 0:
            modificar_cap_transporte(id_transporte=jd['id_transporte'],refrigeracion=jd['refrigeracion'],cap_carga=jd['cap_carga'],cap_tamano=jd['cap_tamano'],usuario_id_usuario=jd['usuario_id_usuario'])            
            datos={'message' : "Exitoso"}
            
        else:
            datos={'message' : "Transporte no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id_transporte):
        jd = json.loads(request.body)
        Transportes = list(CapTransporte.objects.filter(id_transporte=id_transporte).values())
        if len(Transportes) > 0:
            eliminar_cap_transporte(id_transporte=id_transporte)
            datos={'message' : "Exitoso"}
        else:
            datos={'message' : "Transporte no encontrado ..."}
        return JsonResponse(datos)

class TransporteViewset(viewsets.ModelViewSet):
    queryset = CapTransporte.objects.filter()
    serializer_class = Transporte_srlzr


class TransporteAllViewset(viewsets.ModelViewSet):
    queryset = CapTransporte.objects.all()
    serializer_class = Transporte_allsrlzr