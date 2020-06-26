from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from Rutas import views

app_name = 'Rutas'

urlpatterns = [
    path('', views.rutasT, name='rutasT'),
    path('tablaRutasT/', views.tablaRutasT, name='tablaRutasT'),
    path('crearRutaT/',views.crearRutaT,name = "crearRutaT"),
    path('actualizarRutaT/<int:idR>/',views.actualizarRutaT,name = "actualizarRutaT"),
    path('IdCdRuta/',views.IdCdRuta,name = "IdCdRuta"),
    path('borrarRutaT/',views.borrarRutaT,name = "borrarRutaT"),

    #path('', views.rutas, name='rutas'),
    #path('tablaRutas/', views.tablaRutas, name='tablaRutas'),
    #path('crearRuta/',views.crearRuta,name = "crearRuta"),
    #path('selectTransportistasRutas/',views.selectTransportistasRutas,name = "selectTransportistasRutas"),
    #path('selectTiposUnidadesTransportista/',views.selectTiposUnidadesTransportista,name = "selectTiposUnidadesTransportista"),
    #path('actualizarRuta/<int:idT>/<int:idR>/',views.actualizarRuta,name = "actualizarRuta"),
    #path('selectTipoUnidadActualizar/',views.selectTipoUnidadActualizar,name = "selectTipoUnidadActualizar"),
    #path('borrarRuta/',views.borrarRuta,name = "borrarRuta"),
]
