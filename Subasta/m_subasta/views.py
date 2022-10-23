from .models import *
from django.db import connection
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class subastaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0):
            subastas=list(Subasta.objects.filter(id_subasta=id).values())
            if len(subastas)>0:
                subasta = subastas[0]
                datos = {'message' : "Succes" , 'subasta':subasta}
            else:
                datos={'message' : "Subasta no encontrada ..."}
            return JsonResponse(datos)
        else:
            subastas=list(Subasta.objects.values())
            if len(subastas)>0:
                datos={'message' : "Succes" , 'subastas':subastas}
            else:
                datos={'message' : "Subasta no encontrada ..."}

            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        Subasta.objects.create(id_subasta=jd['id_subasta'],fecha_publicacion=jd['fecha_publicacion'],
        fecha_termino_sub=jd['fecha_termino_sub'],cond_carga=jd['cond_carga'],
        cond_tamano=jd['cond_tamano'],cond_refrigeracion=jd['cond_refrigeracion'], valor_inicial=jd['valor_inicial'],
        ultima_puja=jd['ultima_puja'],ctdad_pujas=jd['ctdad_pujas'], pdv_id_pdv=jd['pdv_id_pdv'],
        estado_sub=jd['estado_sub'],cap_transporte_id_transporte=jd['cap_transporte_id_transporte'] )
        datos={'message' : "Succes"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        subastas = list(Subasta.objects.filter(id_subasta=id).values())
        if len(subastas) > 0:
            subasta=Subasta.objects.get(id_subasta=id)
            subasta.id_subasta=jd['id_subasta']
            subasta.fecha_publicacion=jd['fecha_publicacion']
            subasta.fecha_termino_sub=jd['fecha_termino_sub']
            subasta.cond_carga=jd['cond_carga']
            subasta.cond_tamano=jd['cond_tamano']
            subasta.cond_refrigeracion=jd['cond_refrigeracion']
            subasta.valor_inicial=jd['valor_inicial']
            subasta.ultima_puja=jd['ultima_puja']
            subasta.ctdad_pujas=jd['ctdad_pujas']
            subasta.pdv_id_pdv=jd['pdv_id_pdv']
            subasta.estado_sub=jd['estado_sub']
            subasta.cap_transporte_id_transporte=jd['cap_transporte_id_transporte']
            subasta.save()
            datos={'message' : "Succes"}
            
        else:
            datos={'message' : "Subasta no encontrada ..."}
        return JsonResponse(datos)

    def delete(self,request, id):
        subastas = list(Subasta.objects.filter(id_subasta=id).values())
        if len(subastas) > 0:
            Subasta.objects.filter(id_subasta=id).delete()
            datos={'message' : "Succes"}
        else:
            datos={'message' : "Subasta no encontrada ..."}
        return JsonResponse(datos)