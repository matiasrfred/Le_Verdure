from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .views import * 
from .controllers import *
from django.contrib import messages
from django.db import connection

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
        if request.method == 'PUT':
            id_pdv = request.PUT.get('id_pdv')
            ctdad_necesaria = request.PUT.get('ctdad_necesaria')

            Response = pdv_put(id_pdv,ctdad_necesaria)
            print(Response)
            return redirect(to="pdvext")
        
    except:
        return render(request, 'm_web/pdvext.html',data)

    return render(request, 'm_web/pdvext.html',data)

def pdv_id(request,id_pdv):
    data={'pdvs':pdv_get_id(id_pdv),
    'estadopdvs' :estadopdv_get(),
            'solicitudes':solicitud_get(),
            'productos':producto_get(),
            'calidades' :calidad_get(),
            'usuarios' :usuarios_get(),
    }
    print(pdv_get_id(id_pdv))
    return render(request, 'm_web/modificar_pdv.html',data)

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
    if request.method == 'POST':
        mail = request.POST.get('mail')
        passw = request.POST.get('pass')
        resultados_user = LoginAuthController(mail,passw)
        print(resultados_user)
        if resultados_user['message'] == 'Success':
            respt = resultados_user['usuario']
            request.session['id'] = respt[0]
            request.session['nombre'] = respt[1]
            request.session['apellido'] = respt[2]
            request.session['email'] = respt[3]
            request.session['run'] = respt[5]
            request.session['ciudad_id'] = respt[8]
            request.session['rol'] = respt[9]

        else:
            print("Tu mama es maraka")

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
            Response = solicitud_post(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado_id,producto_id_prod_id,usuario_id_usuario_id)
            
            if Response.status_code == 200:
                messages.success(request,"Agregado Correctamente")
                print(Response)
            else:
                messages.error(request,"No se pudo Agregar correctamente")
                print(Response)
            print(Response)
            return redirect(to="solicitud_compra")
            
    except:
        return render(request, 'm_web/solicitudcompra.html')
    return render(request, 'm_web/solicitudcompra.html',data)





