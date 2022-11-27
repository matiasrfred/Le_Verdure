from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .views import * 
from .controllers import *
from django.contrib import messages
from django.db import connection

# Create your views here.



def home(request):
    if request.method == 'POST':
        cerrar_session(request)
    data = obtener_session(request)
    return render(request, 'm_web/home.html',data)
    
def pdvext(request):
    try:
        data = obtener_session(request)
        if data['rol']!='Vendedor':
            return redirect(to="home")

    except:
        return redirect(to="login")

    try:
        data['pdvs']=pdv_get()
        data['estadopdvs']=estadopdv_get()
        data['solicitudes']=solicitud_get()
        data['calidades']=calidad_get()
        data['usuarios']=usuarios_get()
        data['productos']=producto_get()

    except:
        return render(request, 'm_web/pdvext.html',data)

    return render(request, 'm_web/pdvext.html',data)

def pdv_id(request,id_pdv):
    try:
        data = obtener_session(request)
        if data['rol']!='Vendedor':
            return redirect(to="home")

    except:
        return redirect(to="login")
    try:
        data['pdvs']=pdv_get_id(id_pdv)
        data['estadopdvs']=estadopdv_get()
        data['solicitudes']=solicitud_get()
        data['calidades']=calidad_get()
        data['usuarios']=usuarios_get()
        data['productos']=producto_get()

    except:
        return render(request, 'm_web/modificar_pdv.html',data)
    
    return render(request, 'm_web/modificar_pdv.html',data)

def login(request):
    return render(request, 'm_web/home.html')

def productores(request):
    try:
        data = obtener_session(request)
        if data['rol']!='Transportista':
            return redirect(to="home")

    except:
        return redirect(to="login")
    return render(request, 'm_web/productores.html')

def subasta(request):
    try:
        data = obtener_session(request)
        if data['rol']!='Vendedor':
            return redirect(to="home")
    except:
        return redirect(to="login")
    try:
        data['subastas']=subasta_get()
        data['pdvs']=pdv_get()
        data['Transportes']=transporte_get()
        data['solicitudes']=solicitud_get()

    except:
        return render(request, 'm_web/subasta.html')
    return render(request, 'm_web/subasta.html', data)


def productos(request):
    try:
        data = obtener_session(request)
        if data['rol']!='Vendedor':
            return redirect(to="home")

    except:
        return redirect(to="login")

    try:
        data['productos']=producto_get()
        data['calidades']=calidad_get()
        data['Transportes']=transporte_get()
        data['solicitudes']=solicitud_get()

    except:
        return render(request, 'm_web/productos.html',data)
    return render(request, 'm_web/productos.html',data)

def login(request):
    try:
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
                return redirect(to="home")

            else:
                return render(request, 'm_web/home.html')
    except:
        return render(request, 'm_web/home.html')

    return render(request, 'm_web/login.html')



def pdvint(request):
    return render(request, 'm_web/pdvint.html')

@csrf_exempt
def solicitud_compra(request):
    try:
        data = obtener_session(request)
        if data['rol']!='Vendedor':
            return redirect(to="home")

    except:
        return redirect(to="login")

    try:
        data['solicitudes']=solicitud_get()
        data['estadosolicitudes']=estadosolicitud_get()
        data['productos']=producto_get()
        data['calidades']=calidad_get()
        data['usuarios']=usuarios_get()

        if request.method == 'POST':
            fecha_solicitud = request.POST.get('fecha_solicitud')
            ctdad_necesaria = request.POST.get('ctdad_necesaria')
            estado_solicitud_id_estado_id = request.POST.get('estado_solicitud_id_estado_id')
            producto_id_prod_id = request.POST.get('producto_id_prod_id')
            usuario_id_usuario_id = request.POST.get('usuario_id_usuario_id')
            Response = solicitud_post(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado_id,producto_id_prod_id,usuario_id_usuario_id)
            print(fecha_solicitud,ctdad_necesaria,estado_solicitud_id_estado_id,producto_id_prod_id,usuario_id_usuario_id)
            if Response.status_code == 200:
                messages.success(request,"Agregado Correctamente")
                print(Response)
            else:
                messages.error(request,"No se pudo Agregar correctamente")
                print(Response)
            print(Response)
            return redirect(to="solicitud_compra")
            
    except:
        return render(request, 'm_web/solicitudcompra.html',data)
    return render(request, 'm_web/solicitudcompra.html',data)





