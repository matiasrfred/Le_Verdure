from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .controllers import *
# Create your views here.

def home(request):
    return render(request, 'm_web/home.html')
    
def pdvext(request):
    try:
        data = {
            'pdvs':pdv_get(),
            'estadopdvs' :estadopdv_get(),
            'solicitudes':solicitud_get(),
            'productos':producto_get(),
            'calidades' :calidad_get(),
            'usuarios' :usuarios_get(),
            
        }
    except:
        return render(request, 'm_web/pdvext.html')

    return render(request, 'm_web/pdvext.html',data)

def login(request):
    return render(request, 'm_web/login.html')

def productores(request):
    return render(request, 'm_web/productores.html')

def subasta(request):
    try:
        data = {
            'subastas':subasta_get(),
            'pdvs':pdv_get(),
            'Transportes':transporte_get(),
            'solicitudes':solicitud_get(),
        }
    except:
        return render(request, 'm_web/subasta.html')
    return render(request, 'm_web/subasta.html', data)


def productos(request):
    try:
        data = {
            'productos':producto_get(),
            'calidades':calidad_get(),
        }
    except:
        return render(request, 'm_web/productos.html')
    return render(request, 'm_web/productos.html',data)

    

def login(request):
    return render(request, 'm_web/login.html')



def pdvint(request):
    return render(request, 'm_web/pdvint.html')

@csrf_exempt
def solicitud_compra(request):
    try:
        data = {
            'solicitudes':solicitud_get(),
            'estadosolicitudes':estadosolicitud_get(),
            'productos':producto_get(),
            'calidades' :calidad_get(),
            'usuarios' :usuarios_get(),
        }
        if request.method == 'POST':
            fecha_solicitud = request.POST.get('fecha_solicitud')
            ctdad_necesaria = request.POST.get('ctdad_necesaria')
            estado_solicitud_id_estado_id = request.POST.get('estado_solicitud_id_estado_id')
            producto_id_prod_id = request.POST.get('producto_id_prod_id')
            usuario_id_usuario_id = request.POST.get('usuario_id_usuario_id')
            print(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado_id,producto_id_prod_id,usuario_id_usuario_id)
            Response = solicitud_post(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado_id,producto_id_prod_id,usuario_id_usuario_id)
            print(Response)
    except:
        return render(request, 'm_web/solicitudcompra.html')
    return render(request, 'm_web/solicitudcompra.html',data)





