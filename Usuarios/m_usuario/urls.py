from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario',UsuarioViewset,UsuarioAllViewset)
router.register('usuario_all',UsuarioAllViewset)

urlpatterns=[
    path('usuarios/', UsuarioView.as_view(), name='usuarios_lista'),
    path('usuarios/<int:id_usuario>', UsuarioView.as_view(), name='usuarios_proces'),
    path('roles/', RolView.as_view(), name='rol_lista'),
    path('roles/<int:id_rol>', RolView.as_view(), name='rol_proces'),
    path('paises/', PaisView.as_view(), name='pais_lista'),
    path('paises/<int:id_pais>', PaisView.as_view(), name='pais_proces'),
    path('estados/', EstadosView.as_view(), name='estado_lista'),
    path('estados/<int:id_estado>', EstadosView.as_view(), name='estado_proces'),
    path('ciudades/', CiudadView.as_view(), name='ciudad_lista'),
    path('ciudades/<int:id_ciudad>', CiudadView.as_view(), name='ciudad_proces'),
    path('transporte/', TransporteView.as_view(), name='transporte_lista'),
    path('transporte/<int:id_transporte>', TransporteView.as_view(), name='transporte_proces'),   
]
