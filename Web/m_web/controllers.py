import requests
import json

#PRODUCTOS CONTROLLERS
def crear_oferta(id_oferta,precio_oferta,ctdad_ofertada,seleccion,pdv_id_pdv,usuario_id_usuario):
    url = 'http://127.0.0.1:8003/api/ofertantes/'
    body ={'id_oferta':id_oferta,'precio_oferta':precio_oferta,'ctdad_ofertada':ctdad_ofertada,'seleccion':seleccion,'pdv_id_pdv':pdv_id_pdv,'usuario_id_usuario':usuario_id_usuario}
    response=requests.post(url,data=body)
    return response

def solicitud_post(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado,producto_id_prod,usuario_id_usuario):
    url = 'http://127.0.0.1:8002/api/solicitudes/'
    body ={'fecha_solicitud':fecha_solicitud,'ctdad_necesaria':ctdad_necesaria,'estado_solicitud_id_estado_id':estado_solicitud_id_estado,'producto_id_prod_id':producto_id_prod,'usuario_id_usuario_id':usuario_id_usuario}
    response=requests.post(url,data=body)
    return response

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