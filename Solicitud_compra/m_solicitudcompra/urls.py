from django.urls import path
from .views import solicitudView


urlpatterns=[
    path('solicitud/', solicitudView.as_view(), name='solicitud_list'),
    path('solicitud/<int:id>', solicitudView.as_view(), name='solicitud_proces')

]