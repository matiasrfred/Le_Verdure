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

def pdv_put(id_pdv,fecha_termino,estado_pdv_id_estadopdv_id,solicitud_compra_id_solicitud_id,tipo_local):
    url='http://127.0.0.1:8003/api/pdvs/'
    body = {
        "id_pdv": str(id_pdv),
        "fecha_termino": str(fecha_termino),
        "estado_pdv_id_estadopdv_id":str(estado_pdv_id_estadopdv_id),
        "solicitud_compra_id_solicitud_id":str(solicitud_compra_id_solicitud_id),
        "tipo_local": str(tipo_local)
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