from rest_framework import serializers
from .models import Contrato


class Contrato_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ['fecha_inicio','fecha_termino','contrato_activo','usuario_id_usuario']


class Contrato_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Contrato
        fields = '__all__'