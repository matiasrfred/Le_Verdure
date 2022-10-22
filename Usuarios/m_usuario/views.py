import json
from unicodedata import name
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from django.http.response import JsonResponse
import json


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

