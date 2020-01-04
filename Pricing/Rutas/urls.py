from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import routes,loadCarriers,routesUpdate
from Rutas import views

app_name = 'Rutas'

urlpatterns = [
    path('', routes, name='routes'),
    path('loadCarriers',loadCarriers, name='loadCarriers'),
    path('routesUpdate/<int:id>/',routesUpdate, name='routesUpdate'),
    
]
