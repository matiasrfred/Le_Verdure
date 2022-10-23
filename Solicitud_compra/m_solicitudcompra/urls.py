from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('solicitud',SolicitudViewset,SolicitudAllViewset)
router.register('solicitud_all',SolicitudAllViewset)

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