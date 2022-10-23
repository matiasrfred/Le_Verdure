from django.urls import path
from .views import pdvView


urlpatterns=[
    path('pdvs/', pdvView.as_view(), name='pdvs_list'),
    path('pdvs/<int:id>', pdvView.as_view(), name='pdvs_proces')
]