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