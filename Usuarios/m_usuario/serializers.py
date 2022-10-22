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

class Pais_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['n_pais']

class Pais_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Pais
        fields = '__all__'

class Estados_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = ['n_estado','pais_id_pais']

class Estados_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Estados
        fields = '__all__'

class Ciudad_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['n_ciudad','estados_id_estado']

class Ciudad_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Ciudad
        fields = '__all__'

class Rol_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['n_rol']

class Rol_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Rol
        fields = '__all__'

