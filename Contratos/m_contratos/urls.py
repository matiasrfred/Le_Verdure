from django.urls import path
from .views import ContratoView,ContratoViewset,ContratoAllViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('contrato',ContratoViewset,ContratoAllViewset)
router.register('contrato_all',ContratoAllViewset)

urlpatterns=[
    path('contratos/', ContratoView.as_view(), name='contratos_list'),
    path('contratos/<int:id_contrato>', ContratoView.as_view(), name='contratos_proces')
] 