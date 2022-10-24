import requests
import json

"""#PEDIDO CONTROLLERS
def pedido_get():
    url = 'http://127.0.0.1:8002/api/solicitud/'
    try: 
        r = requests.get(url)
    except:
        data = {'message':'error de conexion'}
        return data
    if r.status_code == 200:
        content = json.loads(r.content)
        return content"""

def crear_producto(id_prod,n_prod,ruta_imagen,calidad_id_calidad)