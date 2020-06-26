from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from TransportistasProspecto import views

app_name = 'TransportistasProspecto'

urlpatterns = [
    path('', views.transportistas, name='transportistas'),
   
    #Rutas Filtro
    path('selectRutasFiltro/', views.selectRutasFiltro, name='selectRutasFiltro'),
    path('selectTipoUnidadesFiltro/', views.selectTipoUnidadesFiltro, name='selectTipoUnidadesFiltro'),
    path('filtroCortoG/', views.filtroCortoG, name='filtroCortoG'),
    path('filtroLargoG/', views.filtroLargoG, name='filtroLargoG'),

    #Transportista
    path('tablaTransportistasG/', views.tablaTransportistasG, name='tablaTransportistasG'),
    #Crea transportista
    path('crearTransportistaG/',views.crearTransportistaG,name="crearTransportistaG"),
    path('selectPrioridadesG/',views.selectPrioridadesG,name="selectPrioridadesG"),
    path('selectEstatusG/',views.selectEstatusG,name="selectEstatusG"),
    path('checkboxTiposG/',views.checkboxTiposG,name="checkboxTiposG"),
    #Actualizar transportista
    path('actualizarTransportistaG/<int:idT>/',views.actualizarTransportistaG,name = "actualizarTransportistaG"),
    path('selectPrioridadesActualizarG/',views.selectPrioridadesActualizarG,name="selectPrioridadesActualizarG"),
    path('selectEstatusActualizarG/',views.selectEstatusActualizarG,name="selectEstatusActualizarG"),
    path('checkboxTiposActualizarG/',views.checkboxTiposActualizarG,name="checkboxTiposActualizarG"),
    #Borrar transportista
    path('borrarTransportistaG/',views.borrarTransportistaG,name = "borrarTransportistaG"),

    #Crear tarifa en transportista
    path('crearTarifaG/<int:idT>/',views.crearTarifaG,name = "crearTarifaG"),
    path('selectRutasG/',views.selectRutasG,name = "selectRutasG"),
    path('selectTiposUnidadesTransportistaG/',views.selectTiposUnidadesTransportistaG,name = "selectTiposUnidadesTransportistaG"),
    path('buscarDatosRutaG/',views.buscarDatosRutaG,name = "buscarDatosRutaG"),
    #Actualizar tarifa del transportista
    path('actualizarTarifaG/<int:idT>/<int:idTa>/',views.actualizarTarifaG,name = "actualizarTarifaG"),
    path('selectRutasActualizarG/',views.selectRutasActualizarG,name = "selectRutasActualizarG"),
    path('selectTiposUnidadesTransportistaActualizarG/',views.selectTiposUnidadesTransportistaActualizarG,name = "selectTiposUnidadesTransportistaActualizarG"),
    path('buscarDatosRutaActualizarG/',views.buscarDatosRutaActualizarG,name = "buscarDatosRutaActualizarG"),
    #Borrar ruta en transportista
    path('borrarTarifaG/',views.borrarTarifaG,name = "borrarTarifaG"),

    #Asignar tipo unidad a transportista
    path('asignarTipoUnidadG/<int:idT>/',views.asignarTipoUnidadG,name = "asignarTipoUnidadG"),
    path('selectTiposUnidadesG/',views.selectTiposUnidadesG,name = "selectTiposUnidadesG"),
    #Borrar el tipo de unidad en el transportista
    path('borrarTipoUnidadG/<int:idT>/<int:idU>/',views.borrarTipoUnidadG,name = "borrarTipoUnidadG"),
    path('selectTipoUnidadBorraG/',views.selectTipoUnidadBorraG,name = "selectTipoUnidadBorraG"),

    #Agregar certificacion a transportista
    path('asignarCertificacionG/<int:idT>/',views.asignarCertificacionG,name = "asignarCertificacionG"),
    path('selectCertificacionesG/',views.selectCertificacionesG,name = "selectCertificacionesG"),
    #Borrar certificacion a transportista
    path('borrarCertificacionG/<int:idT>/<int:idC>/',views.borrarCertificacionG,name = "borrarCertificacionG"),
    path('selectCertificacionBorrarG/',views.selectCertificacionBorrarG,name = "selectCertificacionBorrarG"),
    
    #Crear contacto a transportista
    path('crearContactoG/<int:idT>/',views.crearContactoG,name = "crearContactoG"),
    #Actualizar contacto a transportista
    path('actualizarContactoG/<int:idT>/<int:idCO>/',views.actualizarContactoG,name = "actualizarContactoG"),
    #Borrar contacto a transportista
    path('borrarContactoG/',views.borrarContactoG,name = "borrarContactoG"),



    #Contactos
    path('contactos', views.contactos, name='contactos'),
    path('tablaContactos/', views.tablaContactos, name='tablaContactos'),
    path('crearContacto/', views.crearContacto, name="crearContacto"),
    path('selectTransportistasContactos/', views.selectTransportistasContactos, name="selectTransportistasContactos"),
    path('actualizarContacto/<int:idT>/<int:idCO>/',views.actualizarContacto,name = "actualizarContacto"),
    path('borrarContacto/',views.borrarContacto,name = "borrarContacto"),


    #Tipos de Unidades
    path('tiposUnidades', views.tiposUnidades, name='tiposUnidades'),
    path('tablaTiposUnidades/', views.tablaTiposUnidades, name="tablaTiposUnidades"),
    path('crearTipoUnidad/', views.crearTipoUnidad, name="crearTipoUnidad"),
    path('selectCategoriasEjes/', views.selectCategoriasEjes, name="selectCategoriasEjes"),
    path('actualizarTipoUnidad/<int:idTU>/',views.actualizarTipoUnidad,name = "actualizarTipoUnidad"),
    path('selectActualizarTipoUnidad/',views.selectActualizarTipoUnidad,name = "selectActualizarTipoUnidad"),
    path('borrarTipoUnidad/',views.borrarTipoUnidad,name = "borrarTipoUnidad"),


    #Certificaciones
    path('certificaciones', views.certificaciones, name="certificaciones"),
    path('tablaCertificaciones/', views.tablaCertificaciones, name="tablaCertificaciones"),
    path('crearCertificacion/', views.crearCertificacion, name="crearCertificacion"),
    path('actualizarCertificacion/<int:idCer>/', views.actualizarCertificacion, name="actualizarCertificacion"),
    path('borrarCertificacion/', views.borrarCertificacion, name="borrarCertificacion"),
]
