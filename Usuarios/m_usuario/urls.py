from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios',UsuarioViewset,UsuarioAllViewset)
router.register('usuarios_todos',UsuarioAllViewset)
router.register('roles',RolViewset,RolAllViewset)
router.register('roles_todos',RolAllViewset)
router.register('paises',PaisViewset,PaisAllViewset)
router.register('paises_todos',PaisAllViewset)
router.register('estados',EstadosViewset,EstadosAllViewset)
router.register('estados_todos',EstadosAllViewset)
router.register('ciudades',CiudadViewset,CiudadAllViewset)
router.register('ciudades_todos',CiudadAllViewset)
router.register('transporte',TransporteViewset,TransporteAllViewset)
router.register('transporte_todos',TransporteAllViewset)

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
    path('LoginAuth/', LoginAuthView.as_view(), name='LoginAuth')
]
