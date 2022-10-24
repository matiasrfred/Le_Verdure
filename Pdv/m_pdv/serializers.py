from rest_framework import serializers
from .models import *

class Pdv_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Pdv
        fields = ['fecha_comienzo','fecha_termino','ctdad_reunida','precio_total','estado_pdv_id_estadopdv','solicitud_compra_id_solicitud','tipo_local']


class Pdv_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Pdv
        fields = '__all__'


class EstadoPdv_srlzr(serializers.ModelSerializer):
    class Meta:
        model = EstadoPdv
        fields = ['d_estadopdv']

class EstadoPdv_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = EstadoPdv
        fields = '__all__'

class Ofertante_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Ofertantes
        fields = ['precio_oferta,ctdad_ofertada,seleccion,pdv_id_pdv,usuario_id_usuario']

class Ofertante_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Ofertantes
        fields = '__all__'