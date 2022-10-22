from rest_framework import serializers
from .models import *

class Usuario_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','email','run','rol_id_rol','ciudad_id_ciudad']



class Usuario_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'