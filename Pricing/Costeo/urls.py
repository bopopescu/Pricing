from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import (Home, costeos, updateCosteo, loadCosteo, firstTime)
from Costeo import views

app_name = 'Costeo'

urlpatterns = [
    path('Home', Home, name='Home'),

    path('', costeos, name='costeos'),
    path('tablaCostos/', views.tablaCostos, name='tablaCostos'),
    path('excelGeneral/', views.excelGeneral, name="excelGeneral"),
    path('excelCosteo/<int:id>/', views.excelCosteo, name='excelCosteo'),
    path('pdfCosteo/<int:id>/', views.pdfCosteo, name='pdfCosteo'),
    path('hojaPdfCosteo/<int:id>/', views.hojaPdfCosteo, name='hojaPdfCosteo'),


    path('selectRutasCosto/', views.selectRutasCosto, name='selectRutasCosto'),
    path('buscarRutaCosto/', views.buscarRutaCosto, name='buscarRutaCosto'),
    path('selectTiposUnidadesCosto/', views.selectTiposUnidadesCosto, name='selectTiposUnidadesCosto'),
    path('selectModelosCosteo/', views.selectModelosCosteo, name='selectModelosCosteo'),

    #Rutas Filtro En Costo
    path('selectRutasFiltroCostos/', views.selectRutasFiltroCostos, name='selectRutasFiltroCostos'),
    path('selectTipoUnidadesFiltroCostos/', views.selectTipoUnidadesFiltroCostos, name='selectTipoUnidadesFiltroCostos'),
    path('filtroCortoCostos/', views.filtroCortoCostos, name='filtroCortoCostos'),
    path('filtroLargoCostos/', views.filtroLargoCostos, name='filtroLargoCostos'),

    path('updateCosteo/<int:id>/', updateCosteo, name="updateCosteo"),
    path('selectRutasCostoActualizar/', views.selectRutasCostoActualizar, name='selectRutasCostoActualizar'),
    path('buscarRutaCostoActualizar/', views.buscarRutaCostoActualizar, name='buscarRutaCostoActualizar'),
    path('selectTiposUnidadesCostoActualizar/', views.selectTiposUnidadesCostoActualizar, name='selectTiposUnidadesCostoActualizar'),
    path('selectModelosCosteoActualizar/', views.selectModelosCosteoActualizar, name='selectModelosCosteoActualizar'),

    path('borrarCosto/<int:id>/', views.borrarCosto, name='borrarCosto'),

    path('IdCdCosto/',views.IdCdCosto,name = "IdCdCosto"),

    path('loadCosteo/<int:id>/', loadCosteo, name="loadCosteo"),
    path('firstTime/', firstTime, name="firstTime"),
]
