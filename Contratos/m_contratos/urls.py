from django.urls import path
from .views import contratoView


urlpatterns=[
    path('contratos/', contratoView.as_view(), name='contratos_list'),
    path('contratos/<int:id>', contratoView.as_view(), name='contratos_proces')
] 