import requests
import json
from django.http import HttpResponse

#PRODUCTOS CONTROLLERS
def crear_oferta(id_oferta,precio_oferta,ctdad_ofertada,seleccion,pdv_id_pdv,usuario_id_usuario):
    url = 'http://127.0.0.1:8003/api/ofertantes/'
    body ={'id_oferta':id_oferta,'precio_oferta':precio_oferta,'ctdad_ofertada':ctdad_ofertada,'seleccion':seleccion,'pdv_id_pdv':pdv_id_pdv,'usuario_id_usuario':usuario_id_usuario}
    response=requests.post(url,data=body)
    return response

def solicitud_post(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado,producto_id_prod,usuario_id_usuario):
    url = 'http://127.0.0.1:8002/api/solicitudes/'
    body ={
        "fecha_solicitud": str(fecha_solicitud),
        "ctdad_necesaria": str(ctdad_necesaria),
        "estado_solicitud_id_estado_id": str(estado_solicitud_id_estado),
        "producto_id_prod_id": str(producto_id_prod),
        "usuario_id_usuario_id": str(usuario_id_usuario) 
    }
    response=requests.post(url,json=body)
    return response

def LoginAuthController(email,passw):
    url = 'http://127.0.0.1:8000/api/LoginAuth/'
    body ={
        "email": str(email),
        "passw": str(passw)
    }
    response=requests.post(url,json=body)
    if response.status_code == 200:
        content = json.loads(response.content)
        return content

def cerrar_session(request):
    try:
        del request.session['nombre']
        del request.session['apellido']
        del request.session['email']
        del request.session['run']
        del request.session['ciudad_id']
        del request.session['rol']

    except:
        pass
        return HttpResponse("Has cerrado Session")

def obtener_session(request):
    try:
        data={
            'id':request.session['id'],
            'nombre':request.session['nombre'],
            'apellido': request.session['apellido'],
            'email': request.session['email'],
            'run':request.session['run'],
            'ciudad_id':request.session['ciudad_id'],
            'rol': request.session['rol'],}
    except:
        data={'rol':'Visita'}
        
    return data

def subasta_get():
    url = 'http://127.0.0.1:8004/api/subastas/'
    try: 
        r = requests.get(url)
    except:
        data = {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content = json.loads(r.content)
        return content['subastas']

def transporte_get():
    url = 'http://127.0.0.1:8000/api/transporte/'
    try: 
        r = requests.get(url)
    except:
        data = {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content = json.loads(r.content)
        return content['Transportes']

def producto_get():
    url = 'http://127.0.0.1:8002/api/productos/'
    try: 
        r = requests.get(url)
    except:
        data = {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content = json.loads(r.content)
        return content['productos']

def producto_post(n_prod,ruta_imagen,calidad_id_calidad_id,producto_activo):
    url = 'http://127.0.0.1:8002/api/productos/'
    body ={
        "n_prod": str(n_prod),
        "ruta_imagen": str(ruta_imagen),
        "calidad_id_calidad_id": str(calidad_id_calidad_id),
        "producto_activo": str(producto_activo)
    }
    response=requests.post(url,json=body)
    return response


def pdv_get():
    url='http://127.0.0.1:8003/api/pdvs/'
    try:
        r=requests.get(url)
    except:
        data = {'message':'Error de conexion'}
        return data
    if r.status_code == 200:
        content=json.loads(r.content)
        return content['pdvs']

def pdv_get_id(id_pdv):
    url='http://127.0.0.1:8003/api/pdvs/'+ str(id_pdv)
    try:
        r=requests.get(url)
    except:
        data = {'message':'Error de conexion'}
        return data
    if r.status_code == 200:
        content=json.loads(r.content)
    return content['pdv']

def pdv_put(id_pdv,ctdad_reunida,precio_total):
    url='http://127.0.0.1:8003/api/pdvs/'+ str(id_pdv)
    body = {
        "id_pdv": str(id_pdv),
        "ctdad_reunida":str(ctdad_reunida),
        "precio_total":str(precio_total)
    }
    response=requests.put(url,json=body)
    return response

def solicitud_get():
    url = 'http://127.0.0.1:8002/api/solicitudes/'
    try: 
        r = requests.get(url)
    except:
        data = {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content = json.loads(r.content)
        return content['solicitudes']

def estadosolicitud_get():
    url = 'http://127.0.0.1:8002/api/estadosolicitudes/'
    try: 
        r = requests.get(url)
    except:
        data = {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content = json.loads(r.content)
        return content['estadosolicitudes']

def calidad_get():
    url='http://127.0.0.1:8002/api/calidades/'
    try:
        r=requests.get(url)
    except:
        data = {'message':'Error de conexion'}
        return data
    if r.status_code == 200:
        content=json.loads(r.content)
        return content['calidades']

def usuarios_get():
    url='http://127.0.0.1:8000/api/usuarios/'
    try:
        r=requests.get(url)
    except:
        data = {'message':'Error de conexion'}
        return data
    if r.status_code == 200:
        content=json.loads(r.content)
        return content['usuarios']

def estadopdv_get():
    url = 'http://127.0.0.1:8003/api/estadopdvs/'
    try: 
        r = requests.get(url)
    except:
        data = {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content = json.loads(r.content)
        return content['estadopdvs']

def cap_transporte_post(refrigeracion,cap_carga,cap_tamano,usuario_id_usuario_id):
    url = 'http://127.0.0.1:8000/api/transporte/'
    body ={
        "refrigeracion": str(refrigeracion),
        "cap_carga": str(cap_carga),
        "cap_tamano": str(cap_tamano),
        "usuario_id_usuario_id": str(usuario_id_usuario_id)
    }
    response=requests.post(url,json=body)
    return response