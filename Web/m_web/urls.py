from django.urls import path
from .views import home, pdvext, login, pdvopen

urlpatterns = [
    path('', home, name="home"),
    path('pdvext/', pdvext, name="pdvext"),
    path('login/', login, name="login"),
    path('pdvopen/', pdvopen, name="pdvopen"),
]
