import requests
import json
from django.http import HttpResponse

#PRODUCTOS CONTROLLERS
def crear_producto(id_prod,n_prod,ruta_imagen,calidad_id_calidad_id):
    url = 'http://127.0.0.1:8002/api/productos/'
    files = {"ruta_imagen":open(ruta_imagen, "rb")}
    body ={"id_prod":id_prod,"n_prod":n_prod,"ruta_imagen":ruta_imagen,"calidad_id_calidad":calidad_id_calidad_id}
    response=requests.post(url,data=body,files=files)
    return response


def producto_get():
    url = 'http://127.0.0.1:8002/api/productos/'
    try: 
        r = requests.get(url)
    except:
        data = {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content = json.loads(r.content)
        return content

def pdv_get():
    url='http://127.0.0.1:8006/api/pdvs/'
    try:
        r=requests.request.get(url)
    except:
        data= {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content=json.loads(r.content)
        return content
