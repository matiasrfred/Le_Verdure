from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subastas',SubastaViewset,SubastaAllViewset)
router.register('subastas_all',SubastaAllViewset)


urlpatterns=[
    path('subastas/', subastaView.as_view(), name='subastas_list'),
    path('subastas/<int:id>', subastaView.as_view(), name='subastas_proces')
]