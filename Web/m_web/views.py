from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .controllers import *
# Create your views here.

def home(request):
    return render(request, 'm_web/home.html')
    
def pdvext(request):
    data = {
        'pdvs':pdv_get(),
        'estadopdvs' :estadopdv_get(),
        'solicitudes':solicitud_get(),
        'productos':producto_get(),
        'calidades' :calidad_get(),
        'usuarios' :usuarios_get(),
        
    }
    return render(request, 'm_web/pdvext.html',data)

def login(request):
    return render(request, 'm_web/login.html')

def productores(request):
    return render(request, 'm_web/productores.html')

def subasta(request):

    data = {
        'subastas':subasta_get(),
        'pdvs':pdv_get(),
        'Transportes':transporte_get(),
        'solicitudes':solicitud_get(),
    }
    return render(request, 'm_web/subasta.html', data)


def productos(request):
        return render(request, 'm_web/productos.html')

    

def login(request):
    return render(request, 'm_web/login.html')



def pdvint(request):
    return render(request, 'm_web/pdvint.html')

@csrf_exempt
def solicitud_compra(request):
    data = {
        'solicitudes':solicitud_get(),
        'estadosolicitudes':estadosolicitud_get(),
        'productos':producto_get(),
        'calidades' :calidad_get(),
        'usuarios' :usuarios_get(),
    }
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        cantidad = request.POST.get('cantidad')
        estado = request.POST.get('estado')
        producto = request.POST.get('producto')
        usuario = request.POST.get('usuario')
        print(fecha,cantidad,estado,producto,usuario)
        Response = solicitud_post(fecha,cantidad,estado,producto,usuario)
        print(Response)

    return render(request, 'm_web/solicitudcompra.html',data)





