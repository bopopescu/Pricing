from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import (carrier, carrierup,carrierview,carrierDelete,bitacoraDelete,expedienteDelete,carrierUpdate,Unidades,
unitUpdate,unitDelete, loadUnitTypes,unidadType,tarifas,remolques,AddRutas,getRutaAll,remolqueDelete,UpdateUnitType,unitTypeDelete)
from Transportista import views

app_name = 'Transportista'

urlpatterns = [
    path('', carrier, name='carrier'),
    path('info/<int:id>/<int:bandModal>/',carrierview,name = "carrierview" ),
    path('registra/', carrierup, name='carrierup'),
    url(r'^import/', views.import_data, name="import"),
    path('carrierUpdate/<int:id>/',carrierUpdate,name = "carrierUpdate"),
    path('carrierDelete/<int:id>/',carrierDelete,name = "carrierDelete"),
    path('expedienteDelete/<int:id>/<str:campo>/',expedienteDelete,name = "expedienteDelete"),
    path('bitacoraDelete/<int:id>/<int:idtransportista>/',bitacoraDelete,name = "bitacoraDelete"),
   	path('unit/',Unidades,name='Unidades'),
    path('unitType/',unidadType,name='unidadType'),
    path('UpdateUnitType/<int:id>/',UpdateUnitType,name='UpdateUnitType'),
    path('unitTypeDelete/<int:id>/',unitTypeDelete,name='unitTypeDelete'),
   	path('unitUpdate/<int:id>/',unitUpdate,name = "unitUpdate"),
   	path('unitDelete/<int:id>/',unitDelete,name = "unitDelete"),
   	path('loadUnitTypes',loadUnitTypes,name = "loadUnitTypes"),
    path('tarifas',tarifas,name = "tarifas"),
    path('remolques',remolques,name = "remolques"),
    path('getRutaAll',getRutaAll,name = "getRutaAll"),
    path('AddRutas/<int:id>/',AddRutas,name = "AddRutas"),
    path('remolqueDelete/<int:id>/',remolqueDelete,name = "remolqueDelete"),

]
