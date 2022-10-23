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

class estadoSolicitud_srlzr(serializers.ModelSerializer):
    class Meta:
        model = EstadoSolicitud
        fields = ['d_estado']

class estadoSolicitud_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = EstadoSolicitud
        fields = '__all__'

class Calidad_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Calidad
        fields = ['descripcion_c']

class Calidad_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Calidad
        fields = '__all__'

class Producto_srlzr(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['n_prod','ruta_imagen','calidad_id_calidad']

class Producto_allsrlzr(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'