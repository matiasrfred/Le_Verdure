from rest_framework import serializers
from .models import *

class Estadisticas_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Estadisticas
        fields = ['nombre','apellido','email','run','rol_id_rol','ciudad_id_ciudad']



class Estadisticas_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Estadisticas
        fields = '__all__'