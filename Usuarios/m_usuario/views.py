import json
from unicodedata import name
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario,Pais
from django.http.response import JsonResponse
from django.db import connection
import cx_Oracle

# Create your views here.
##############################################

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

def eliminar_pais(n_pais):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_PAIS',[n_pais,salida])

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

def eliminar_estado(n_estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_ESTADOS',[n_estado,salida])

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

def eliminar_ciudad(n_ciudad):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_CIUDAD',[n_ciudad,salida])

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

def eliminar_rol(n_rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_ROL',[n_rol,salida])

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

#######################################
#           CLASES VIEWS              #
#######################################

class usuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            usuarios=list(Usuario.objects.filter(id_usuario=id).values())
            if len(usuarios)>0:
                usuario = usuarios[0]
                datos = {'message' : "Succes" , 'usuario':usuario}
            else:
                datos={'message' : "Usuario no encontrado ..."}
            return JsonResponse(datos)
        else:
            usuarios=list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message' : "Succes" , 'usuarios':usuarios}
            else:
                datos={'message' : "Usuario no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        Usuario.objects.create(id_usuario=jd['id_usuario'],nombre=jd['nombre'],apellido=jd['apellido'],email=jd['email'],password=jd['password'],run=jd['run'],usuario_activo=jd['usuario_activo'],superuser=jd['superuser'],ciudad_id_ciudad_id=jd['ciudad_id_ciudad_id'], rol_id_rol_id=jd['rol_id_rol_id'] )
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id_usuario=id).values())
        if len(usuarios) > 0:
            usuario=Usuario.objects.get(id_usuario=id)
            usuario.id_usuario=jd['id_usuario']
            usuario.nombre=jd['nombre']
            usuario.apellido=jd['apellido']
            usuario.email=jd['email']
            usuario.password=jd['password']
            usuario.run=jd['run']
            usuario.usuario_activo=jd['usuario_activo']
            usuario.superuser=jd['superuser']
            usuario.ciudad_id_ciudad_id=jd['ciudad_id_ciudad_id']
            usuario.rol_id_rol_id=jd['rol_id_rol_id']
            usuario.save()
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Usuario no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id):
        usuarios = list(Usuario.objects.filter(id_usuario=id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id_usuario=id).delete()
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Usuario no encontrado ..."}
        return JsonResponse(datos)

###########################################################
class usuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            usuarios=list(Usuario.objects.filter(id_usuario=id).values())
            if len(usuarios)>0:
                usuario = usuarios[0]
                datos = {'message' : "Succes" , 'usuario':usuario}
            else:
                datos={'message' : "Usuario no encontrado ..."}
            return JsonResponse(datos)
        else:
            usuarios=list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message' : "Succes" , 'usuarios':usuarios}
            else:
                datos={'message' : "Usuario no encontrado ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        Usuario.objects.create(id_usuario=jd['id_usuario'],nombre=jd['nombre'],apellido=jd['apellido'],email=jd['email'],password=jd['password'],run=jd['run'],usuario_activo=jd['usuario_activo'],superuser=jd['superuser'],ciudad_id_ciudad_id=jd['ciudad_id_ciudad_id'], rol_id_rol_id=jd['rol_id_rol_id'] )
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id_usuario=id).values())
        if len(usuarios) > 0:
            usuario=Usuario.objects.get(id_usuario=id)
            usuario.id_usuario=jd['id_usuario']
            usuario.nombre=jd['nombre']
            usuario.apellido=jd['apellido']
            usuario.email=jd['email']
            usuario.password=jd['password']
            usuario.run=jd['run']
            usuario.usuario_activo=jd['usuario_activo']
            usuario.superuser=jd['superuser']
            usuario.ciudad_id_ciudad_id=jd['ciudad_id_ciudad_id']
            usuario.rol_id_rol_id=jd['rol_id_rol_id']
            usuario.save()
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Usuario no encontrado ..."}
        return JsonResponse(datos)

    def delete(self,request, id):
        usuarios = list(Usuario.objects.filter(id_usuario=id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id_usuario=id).delete()
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Usuario no encontrado ..."}
        return JsonResponse(datos)
        