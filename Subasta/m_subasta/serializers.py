from rest_framework import serializers
from .models import *

class Subasta_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Subasta
        fields = ['fecha_publicacion','fecha_termino_sub','cond_carga','cond_tamano','cond_refrigeracion','valor_inicial','ultima_puja','ctdad_pujas','pdv_id_pdv','estado_sub','cap_transporte_id_transporte']



class Subasta_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Subasta
        fields = '__all__'