from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('calidades',CalidadViewset,CalidadAllViewset)
router.register('calidades_all',CalidadAllViewset)
router.register('productos',ProductoViewset,ProductoAllViewset)
router.register('productos_all',ProductoAllViewset)
router.register('solicitud',SolicitudViewset,SolicitudAllViewset)
router.register('solicitud_all',SolicitudAllViewset)
router.register('estadoSolicitud',EstadoSolicitudViewset,EstadoSolicitudAllViewset)
router.register('estadoSolicitud_all',EstadoSolicitudAllViewset)

urlpatterns=[
    path('calidades/', CalidadView.as_view(), name='calidad_list'),
    path('calidades/<int:id_calidad>', CalidadView.as_view(), name='calidad_proces'),
    path('productos/', ProductoView.as_view(), name='productos_list'),
    path('productos/<int:id_prod>', ProductoView.as_view(), name='productos_proces'),
    path('solicitudes/', SolicitudView.as_view(), name='solicitud_list'),
    path('solicitudes/<int:id_solicitud>', SolicitudView.as_view(), name='solicitud_proces'),
    path('estadoSolicitud/', estadoSolicitudView.as_view(), name='estadoSolicitud_list'),
    path('estadoSolicitud/<int:id_estado>', estadoSolicitudView.as_view(), name='estadoSolicitud_proces'),
]