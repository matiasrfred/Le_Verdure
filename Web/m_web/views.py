from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .controllers import pdv_get
# Create your views here.

def home(request):
    return render(request, 'm_web/home.html')

def pdvext(request):
    data = {
        'pdv':pdv_get()
    }
    
    return render(request, 'm_web/pdvext.html',data)

def login(request):
    return render(request, 'm_web/login.html')

def productores(request):
    return render(request, 'm_web/productores.html')

def subasta(request):
    return render(request, 'm_web/subasta.html')

@csrf_exempt
def productos(request):
    if request.method == 'POST':
        id_prod = request.POST.get('id-producto')
        n_prod = request.POST.get('nombre-producto')
        ruta_imagen = request.POST.get('imagen-producto')
        calidad_id_calidad_id = request.POST.get('id-calidad')
    else:
        return render(request, 'm_web/productos.html')

    

def login(request):
    return render(request, 'm_web/login.html')



def pdvint(request):
    return render(request, 'm_web/pdvint.html')

def solicitudcompra(request):
    return render(request, 'm_web/solicitudcompra.html')




