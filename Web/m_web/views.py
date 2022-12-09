from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .views import * 
from .controllers import *
from django.contrib import messages
# Create your views here.



def home(request):
    if request.method == 'POST':
        cerrar_session(request)
        messages.success(request,"Sesión Cerrada Correctamente")
    data = obtener_session(request)
    return render(request, 'm_web/home.html',data)
    
def pdvext(request):
    try:
        data = obtener_session(request)
        if data['rol'] == 'Cliente Externo' or 'Productor':
            try:
                data['pdvs']=pdv_get()
                data['estadopdvs']=estadopdv_get()
                data['solicitudes']=solicitud_get()
                data['calidades']=calidad_get()
                data['usuarios']=usuarios_get()
                data['productos']=producto_get()

            except:
                messages.error(request,"No tiene el cargo necesario")
                return redirect(to="home")
        else:
            messages.error(request,"No tiene el cargo necesario")
            return redirect(to="home")
    except:
        print("casi2")
        return redirect(to="login")

    return render(request, 'm_web/pdvext.html',data)

def pdv_id(request,id_pdv):
    try:
        data = obtener_session(request)
        if data['rol']=='Cliente Externo'or'Productor':
            try:
                data['pdvs']=pdv_get_id(id_pdv)
                data['estadopdvs']=estadopdv_get()
                data['solicitudes']=solicitud_get()
                data['calidades']=calidad_get()
                data['usuarios']=usuarios_get()
                data['productos']=producto_get()
            except:
                return render(request, 'm_web/modificar_pdv.html',data)
            if request.method == 'POST':
                id_pdv = request.POST.get('id_pdv')
                ctdad_reunida = request.POST.get('ctdad_reunida')
                precio_total = request.POST.get('precio_total')
                pdv = data['pdvs']
                if int(pdv['ctdad_reunida']) <= int(ctdad_reunida):
                    messages.error(request,"La cantidad no debe exceder la necesaria")

                else:
                    Response = pdv_put(id_pdv,ctdad_reunida,precio_total)
                    print(id_pdv,ctdad_reunida,precio_total)
                    if Response.status_code == 200:
                            messages.success(request,"Modificado Correctamente")
                            print(Response)
                    else:
                        messages.error(request,"No se pudo Agregar correctamente")
                        print(Response)
                    print(Response)
                    return redirect(to='pdvext')
        else:
            messages.error(request,"No tiene el cargo necesario")
            return redirect(to="home")
    except:
        return redirect(to='login')
    return render(request, 'm_web/modificar_pdv.html',data)


def transportista(request):
    try:
        data = obtener_session(request)
        if data['rol']!='Transportista':
            return redirect(to="home")

    except:
        return redirect(to="login")

    try:
        data['Transportes']=transporte_get()
        data['productos']=producto_get()
    except:
        return render(request, 'm_web/productores.html',data)
    return render(request, 'm_web/productores.html',data)

def subasta(request):
    try:
        data = obtener_session(request)
        if data['rol']=='Transportista':
            try:
                data['subastas']=subasta_get()
                data['pdvs']=pdv_get()
                data['Transportes']=transporte_get()
                data['solicitudes']=solicitud_get()
                
            except:
                return render(request, 'm_web/subasta.html',data)
            print("hola")    
        else:
            messages.error(request,"No tiene el cargo necesario")
            return redirect(to="home")

    except:
        print("aa")
        return redirect(to="login")
    
    
    return render(request, 'm_web/subasta.html', data)

@csrf_exempt
def productos(request):
    try:
        data = obtener_session(request)
        if data['rol']=='Productor' or 'Cliente Interno':
            try:
                data['productos']=producto_get()
                data['calidades']=calidad_get()
                print("aca3")

                if request.method == 'POST':
                    n_prod = request.POST.get('n_prod')
                    ruta_imagen = request.POST.get('ruta_imagen')
                    calidad_id_calidad_id = request.POST.get('calidad_id_calidad_id')
                    producto_activo = request.POST.get('producto_activo')
                    Response = producto_post(n_prod,ruta_imagen,calidad_id_calidad_id,producto_activo)
                    print(n_prod,ruta_imagen,calidad_id_calidad_id,producto_activo)
                    if Response.status_code == 200:
                        messages.success(request,"Agregado Correctamente")
                        print(Response)
                    else:
                        messages.error(request,"No se pudo Agregar correctamente")
                        print(Response)
                    print(Response)
                    return redirect(to="productos")

            except:
                print("aca4")
                return render(request, 'm_web/productos.html',data)
        else:
            messages.error(request,"No tiene el cargo necesario")
            return redirect(to="home")
    except:
        print("aca2")
        return redirect(to="home")
    return render(request, 'm_web/productos.html',data)

def login(request):
    try:
        if request.method == 'POST':
            mail = request.POST.get('mail')
            passw = request.POST.get('pass')
            resultados_user = LoginAuthController(mail,passw)
            if resultados_user['message'] == 'Success':
                respt = resultados_user['usuario']
                request.session['id'] = respt[0]
                request.session['nombre'] = respt[1]
                request.session['apellido'] = respt[2]
                request.session['email'] = respt[3]
                request.session['run'] = respt[5]
                request.session['ciudad_id'] = respt[8]
                request.session['rol'] = respt[9]
                messages.success(request,"Logueado Correctamente")
                return redirect(to="home")
                
            else:
                messages.error(request,"No fue posible Loguearte")
                return redirect(to="home")
    except:
        messages.error(request,"No fue posible Loguearte")
        return redirect(to="home")

    return render(request, 'm_web/login.html')



def pdvint(request):
    try:
        data = obtener_session(request)
        if data['rol']!='Cliente Interno':
            return redirect(to="home")

    except:
        return redirect(to="login")

    try:
        data['productos']=producto_get()
        data['calidades']=calidad_get()
        data['Transportes']=transporte_get()
        data['solicitudes']=solicitud_get()

    except:
        return render(request, 'm_web/pdvint.html',data)
    return render(request, 'm_web/pdvint.html',data)

@csrf_exempt
def solicitud_compra(request):
    try:
        data = obtener_session(request)
        if data['rol']=='Cliente Externo':
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

        else:
            messages.error(request,"No tiene el cargo necesario")
            return redirect(to="home")
    except:
        messages.error(request,"No tiene el cargo necesario")
        return redirect(to="home")

    
    return render(request, 'm_web/solicitudcompra.html',data)


def lista_pdv(request,id_pdv):

    try:
        data = obtener_session(request)
        if data['rol']=='Productor':
            try:
                data['pdvs']=pdv_get_id(id_pdv)
                data['estadopdvs']=estadopdv_get()
                data['solicitudes']=solicitud_get()
                data['calidades']=calidad_get()
                data['usuarios']=usuarios_get()
                data['productos']=producto_get()

            except:
                return render(request, 'm_web/pdvext.html',data)
        else:
            messages.error(request,"No tiene el cargo necesario")
            return redirect(to="home")

    except:
        return redirect(to="login")
    return render(request, 'm_web/lista_pdv.html',data)

def cap_transporte(request):
    try:
        data = obtener_session(request)
        if data['rol']=='Transportista':
                try:

                    data['Transportes']=transporte_get()
                    if request.method == 'POST':
                        Refrigeracion = request.POST.get('Refrigeracion')
                        cap_carga = request.POST.get('cap_carga')
                        cap_tamaño = request.POST.get('cap_tamaño')
                        usuario_id_usuario_id = request.POST.get('usuario_id_usuario_id')
                        Response = cap_transporte_post(Refrigeracion,cap_carga,cap_tamaño,usuario_id_usuario_id)
                        print(Refrigeracion,cap_carga,cap_tamaño,usuario_id_usuario_id)
                        if Response.status_code == 200:
                            messages.success(request,"Agregado Correctamente")
                            print(Response)
                        else:
                            messages.error(request,"No se pudo Agregar correctamente")
                            print(Response)
                        print(Response)
                        return redirect(to="transportista")


                except:
                    return render(request, 'm_web/pdvint.html',data)
        else:
            messages.error(request,"No tiene el cargo necesario")
            return redirect(to="home")
    except:
        print("aca")
        return redirect(to="login")
    return render(request, 'm_web/cap_transporte.html',data)



