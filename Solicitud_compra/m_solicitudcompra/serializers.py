from rest_framework import serializers
from .models import *

class Solicitud_srlzr(serializers.ModelSerializer):
    class Meta:
        model = SolicitudCompra
        fields = ['fecha_solicitud','ctdad_necesaria','estado_solicitud_id_estado','producto_id_prod','usuario_id_usuario']



class Solicitud_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = SolicitudCompra
        fields = '__all__'