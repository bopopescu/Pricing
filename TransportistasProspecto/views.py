from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from users import models as Users_models
from .models import TransportistasProspectos, Prioridades, Estatus, Tipos, Certificaciones, Contactos
from Rutas.models import Rutas, TiposUnidades, CategoriasEjes, Tarifas
from Costeo.models import Costeo
from .forms import TransportistaProspectoForm, ActualizarTransportistaProspectoForm, CertificacionesForm, ContactosForm, ActualizarContactosForm, ContactosEnContactosForm, CertificacionesEnCertificacionesForm, ActualizarCertificacionesEnCertificacionesForm
from Rutas.forms import TiposUnidadesForm, TipoUnidadesEnTiposUnidadesForm, ActualizarTipoUnidadesEnTiposUnidadesForm
from Rutas.forms import TarifaForm, ActualizarTarifaForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q
from decimal import Decimal
import requests
import json


def transportistas(request):
    if (request.user.is_authenticated):
        return render(request, "transportistas.html")
    else:
        return HttpResponseRedirect('/')


#Rutas Filtro
def selectRutasFiltro(request):
    if (request.user.is_authenticated):
        data = dict()
        rutas = Rutas.objects.filter(Actividad = 1).order_by('NombreRuta').distinct()
        data['selectRutasFiltro'] = render_to_string('selectRutasFiltro.html', {'rutas': rutas})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectTipoUnidadesFiltro(request):
    if (request.user.is_authenticated):
        tiposUnidades = TiposUnidades.objects.filter(Actividad = 1).order_by('Nombre').all()
        data = dict()
        data['selectTipoUnidadesFiltro'] = render_to_string('selectTipoUnidadesFiltro.html', {'tiposUnidades': tiposUnidades})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def filtroCortoG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        tarifas = Tarifas.objects.filter(IDRuta=datos['IDRuta'], Actividad =1, IDTipoUnidad=datos['IDTipoUnidad'], Precio__range=(Decimal(datos['LimiteInferior']), Decimal(datos['LimiteSuperior']))).all()
        data['filtroCortoG'] = render_to_string('filtrosLC.html', {'tarifas': tarifas})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def filtroLargoG(request):
    if (request.user.is_authenticated):
        request_data = request.POST
        datos = json.loads(request_data['data'])
        data = dict()
        rutas = Rutas.objects.filter(Actividad = 1, CPOrigen = datos['CPOrigen'], EstadoOrigen=datos['EstadoOrigen'], CiudadOrigen=datos['CiudadOrigen'], CPDestino = datos['CPDestino'], EstadoDestino=datos['EstadoDestino'], CiudadDestino=datos['CiudadDestino']).all()
        tarifas = Tarifas.objects.filter(IDRuta= rutas[0], Actividad = 1, IDTipoUnidad=datos['IDTipoUnidad'], Precio__range=(Decimal(datos['LimiteInferior']), Decimal(datos['LimiteSuperior'])))
        data['filtroLargoG'] = render_to_string('filtrosLC.html', {'tarifas': tarifas})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')



#Transportistas
def tablaTransportistasG(request):
    if (request.user.is_authenticated):
        data = dict()
        transportistas=TransportistasProspectos.objects.filter(Actividad = 1).order_by('RazonSocial').select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
        data['tablaTransportistasG'] = render_to_string('tablaTransportistasG.html', {'transportistas': transportistas})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')



#Crea transportista
def crearTransportistaG(request):
    if (request.user.is_authenticated):
        data = dict()
        form = TransportistaProspectoForm()
        crearTransportistaG= "crearTransportistaG/"
        if request.method == "POST":
            form = TransportistaProspectoForm(request.POST)
            if form.is_valid():
                if(TransportistasProspectos.objects.filter(RazonSocial=form.cleaned_data["RazonSocial"], Actividad=1).exists()==True):
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    transportista = TransportistasProspectos(
                        RazonSocial=form.cleaned_data["RazonSocial"],
                        NombreComercial=form.cleaned_data["NombreComercial"],
                        RFC=form.cleaned_data["RFC"],
                        PaginaWeb=form.cleaned_data["PaginaWeb"],
                        Municipio=form.cleaned_data["Municipio"],
                        Estado=form.cleaned_data["Estado"],
                        Pais=form.cleaned_data["Pais"],
                        CodigoPostal=form.cleaned_data["CodigoPostal"],
                        Calle=form.cleaned_data["Calle"],
                        NumeroExt=form.cleaned_data["NumeroExt"],
                        NumeroInt=form.cleaned_data["NumeroInt"],
                        Colonia=form.cleaned_data["Colonia"],
                        Seguridad=form.cleaned_data["Seguridad"],
                        PolizaSeguro=form.cleaned_data["PolizaSeguro"],
                        Credito=form.cleaned_data["Credito"],
                        IDPrioridad = get_object_or_404(Prioridades, pk=form.cleaned_data["IDPrioridad"]),
                        IDEstatus = get_object_or_404(Estatus, pk=form.cleaned_data["IDEstatus"]),
                    )
                    transportista.save()

                    arregloTipos = (request.POST["arregloTipos"]).split(',')
                    for tipo in arregloTipos:
                        if tipo !="":
                            objeto = get_object_or_404(Tipos, pk=tipo)
                            transportista.IDTipo.add(objeto)

                    transportista.save()
                    data['bandera'] = 3
                    return JsonResponse(data)

            data['bandera'] = 4
            return JsonResponse(data)

        data['bandera'] = 1
        context = {'crearTransportistaG':crearTransportistaG,'form': form}
        data['crearTransportistaG'] = render_to_string('crearTransportistaG.html',context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectPrioridadesG(request):
    if (request.user.is_authenticated):
        data = dict()
        prioridades = Prioridades.objects.filter(Actividad = 1).order_by('Nombre').all()
        data['selectPrioridadesG'] = render_to_string('selectPrioridadesG.html',{'prioridades' : prioridades}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectEstatusG(request):
    if (request.user.is_authenticated):
        data = dict()
        estatus = Estatus.objects.filter(Actividad = 1).order_by('Nombre').all()
        data['selectEstatusG'] = render_to_string('selectEstatusG.html',{'estatus' : estatus}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def checkboxTiposG(request):
    if (request.user.is_authenticated):
        data = dict()
        tipos = Tipos.objects.filter(Actividad = 1).order_by('Nombre').all()
        data['checkboxTiposG'] = render_to_string('checkboxTiposG.html',{'tipos' : tipos}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Actualizar transportista
def actualizarTransportistaG(request, idT):
    if (request.user.is_authenticated):
        data = dict()
        transportista = get_object_or_404(TransportistasProspectos, pk=idT)
        colonia = transportista.Colonia
        estatus = transportista.IDEstatus.id
        prioridad = transportista.IDPrioridad.id
        #tipo = transportista.IDTipo.id
        idT = transportista.id
        form = ActualizarTransportistaProspectoForm(request.POST or None, instance=transportista)
        actualizarTransportistaG = "actualizarTransportistaG/"+str(idT)+"/"
        if (request.method == "POST"):
            form = TransportistaProspectoForm(request.POST)
            if form.is_valid():
                if TransportistasProspectos.objects.filter(~Q(id=idT), Actividad = 1).filter(RazonSocial=form.cleaned_data["RazonSocial"], Actividad=1).exists()==True:
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    transportista.RazonSocial=form.cleaned_data["RazonSocial"]
                    transportista.NombreComercial=form.cleaned_data["NombreComercial"]
                    transportista.RFC=form.cleaned_data["RFC"]
                    transportista.PaginaWeb=form.cleaned_data["PaginaWeb"]
                    transportista.Municipio=form.cleaned_data["Municipio"]
                    transportista.Estado=form.cleaned_data["Estado"]
                    transportista.Pais=form.cleaned_data["Pais"]
                    transportista.CodigoPostal=form.cleaned_data["CodigoPostal"]
                    transportista.Calle=form.cleaned_data["Calle"]
                    transportista.NumeroExt=form.cleaned_data["NumeroExt"]
                    transportista.NumeroInt=form.cleaned_data["NumeroInt"]
                    transportista.Colonia=form.cleaned_data["Colonia"]
                    transportista.Seguridad=form.cleaned_data["Seguridad"]
                    transportista.PolizaSeguro=form.cleaned_data["PolizaSeguro"]
                    transportista.Credito=form.cleaned_data["Credito"]
                    transportista.IDPrioridad = get_object_or_404(Prioridades, pk=int(form.cleaned_data["IDPrioridad"]))
                    #transportista.IDTipo = get_object_or_404(Tipos, pk=form.cleaned_data["IDTipo"])
                    transportista.IDEstatus = get_object_or_404(Estatus, pk=form.cleaned_data["IDEstatus"])
                    transportista.save()

                    
                    for tipoT in transportista.IDTipo.all():
                        objeto = get_object_or_404(Tipos, pk=tipoT.id)
                        transportista.IDTipo.remove(objeto)
                    transportista.save()

                    arregloTipos = (request.POST["arregloTipos"]).split(',')
                    for tipo in arregloTipos:
                        if tipo !="":
                            objeto = get_object_or_404(Tipos, pk=tipo)
                            transportista.IDTipo.add(objeto)
                    transportista.save()

                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                data['bandera'] = 4
                return JsonResponse(data)

        data['IDEstatus'] = estatus
        data['IDPrioridad'] = prioridad
        #data['IDTipo'] = tipo
        data['bandera'] = 1
        data['colonia'] = colonia
        data['idT'] = idT
        #context = {'form': form, 'actualizarTransportistaG':actualizarTransportistaG, 'colonia' : colonia, 'idT' : idT}
        context = {'form': form, 'actualizarTransportistaG':actualizarTransportistaG, 'idT' : idT}
        data['actualizarTransportistaG'] = render_to_string('actualizarTransportistaG.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectPrioridadesActualizarG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        prioridades = Prioridades.objects.filter(Actividad = 1).order_by('Nombre').all()
        data['selectPrioridadesActualizarG'] = render_to_string('selectPrioridadesActualizarG.html',{'prioridades' : prioridades, 'IDPrioridad' : datos['IDPrioridad']}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectEstatusActualizarG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        estatus = Estatus.objects.filter(Actividad = 1).order_by('Nombre').all()
        data['selectEstatusActualizarG'] = render_to_string('selectEstatusActualizarG.html',{'estatus' : estatus, 'IDEstatus' : datos['IDEstatus']}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def checkboxTiposActualizarG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        
        arregloTipos = []
        tiposTransportistas = TransportistasProspectos.objects.filter(id=datos['idT'], Actividad = 1).order_by('RazonSocial').select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
        for tipoTransportista in tiposTransportistas[0].IDTipo.all():
            arregloTipos.append(tipoTransportista.id)

        data['arregloTipos'] = arregloTipos
        tipos = Tipos.objects.filter(Actividad = 1).order_by('Nombre').all()
        data['checkboxTiposActualizarG'] = render_to_string('checkboxTiposActualizarG.html',{'tipos' : tipos}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Borrar transportista
def borrarTransportistaG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        transportista = TransportistasProspectos.objects.filter(id = datos['idT'], Actividad = 1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
        Btransportista = get_object_or_404(TransportistasProspectos, pk=datos["idT"])
        
        tarifas = transportista[0].IDTarifa.count()
        tiposUnidades = transportista[0].IDTipoUnidad.count()
        certificaciones = transportista[0].IDCertificacion.count()
        contactos = transportista[0].IDContacto.count()

        if tarifas == 0 and tiposUnidades== 0 and certificaciones == 0 and contactos == 0:
            Btransportista.Actividad = 0
            Btransportista.save()
            data["bandera"] = 1
            return JsonResponse(data)
        else:
            Btransportista.Actividad = 1
            Btransportista.save()
            data["bandera"] = 2
            return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')



#Crear tarifa en transportista
def crearTarifaG(request, idT):
    if (request.user.is_authenticated):
        data = dict()
        crearTarifaG="crearTarifaG/"+str(idT)+"/"
        form = TarifaForm()

        if request.method == "POST":
            form = TarifaForm(request.POST)
            if form.is_valid():
                bandera = 1
                tarifas = TransportistasProspectos.objects.filter(id=idT, Actividad = 1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
                for tarifaC in tarifas[0].IDTarifa.all():
                    if tarifaC.IDRuta.id == form.cleaned_data["IDRuta"] and tarifaC.IDTipoUnidad.id == form.cleaned_data["IDTipoUnidad"] and tarifaC.Precio == form.cleaned_data["Precio"] and tarifaC.ViajeRedondo == form.cleaned_data["ViajeRedondo"]:
                        bandera = 0
                        break
                if bandera == 0:
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    transportista=get_object_or_404(TransportistasProspectos, pk=idT)
                    tarifa = Tarifas(
                        IDTipoUnidad=get_object_or_404(TiposUnidades, pk=form.cleaned_data["IDTipoUnidad"]),
                        IDRuta=get_object_or_404(Rutas, pk=form.cleaned_data["IDRuta"]),
                        Precio=form.cleaned_data["Precio"],
                        ViajeRedondo=form.cleaned_data["ViajeRedondo"],
                    )
                    tarifa.save()
                    transportista.IDTarifa.add(tarifa)
                    transportista.save()
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                print(form.errors)
                data['bandera'] = 4
                return JsonResponse(data)

        context = {'form': form, 'crearTarifaG':crearTarifaG }
        data['crearTarifaG'] = render_to_string('crearTarifaG.html', context, request=request)
        data['bandera'] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectRutasG(request):
    if (request.user.is_authenticated):
        data = dict()
        rutas = Rutas.objects.filter(Actividad = 1).order_by('NombreRuta').all()
        data['selectRutasG'] = render_to_string('selectRutasG.html', {'rutas': rutas})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectTiposUnidadesTransportistaG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        tiposUnidadesT=transportistas=TransportistasProspectos.objects.filter(id=datos["idT"], Actividad = 1).order_by('RazonSocial').select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')

        arregloTiposUnidades = []
        for tipoUnidadT in tiposUnidadesT[0].IDTipoUnidad.order_by("Nombre").all():
            arregloTiposUnidades.append(tipoUnidadT)

        data['selectTiposUnidadesTransportistaG'] = render_to_string('selectTiposUnidadesTransportistaG.html', {'tiposUnidades': arregloTiposUnidades})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def buscarDatosRutaG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        ruta = Rutas.objects.filter(Actividad = 1, id=datos['idR']).all()
        data['CPOrigen'] = ruta[0].CPOrigen
        data['CiudadOrigen'] = ruta[0].CiudadOrigen
        data['EstadoOrigen'] = ruta[0].EstadoOrigen
        data['CPDestino'] = ruta[0].CPDestino
        data['CiudadDestino'] = ruta[0].CiudadDestino
        data['EstadoDestino'] = ruta[0].EstadoDestino
        data['Kilometros'] = ruta[0].Kilometros
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Actualizar tarifa del transportista
def actualizarTarifaG(request, idT, idTa):
    if (request.user.is_authenticated):
        data = dict()
        tarifa = get_object_or_404(Tarifas, pk=idTa)
        ruta = get_object_or_404(Rutas, pk=tarifa.IDRuta.id)
        form = ActualizarTarifaForm(request.POST or None, instance=ruta)
        actualizarTarifaG = "actualizarTarifaG/"+str(idT)+"/"+str(idTa)+"/"
        
        if (request.method == "POST"):
            form = TarifaForm(request.POST)
            if form.is_valid():
                bandera = 1
                tarifas = TransportistasProspectos.objects.filter(id=idT, Actividad = 1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
                for tarifaC in tarifas[0].IDTarifa.all():
                    if tarifaC.id != idTa:
                        if tarifaC.IDRuta.id == form.cleaned_data["IDRuta"] and tarifaC.IDTipoUnidad.id == form.cleaned_data["IDTipoUnidad"] and tarifaC.Precio == form.cleaned_data["Precio"] and tarifaC.ViajeRedondo == form.cleaned_data["ViajeRedondo"]:
                            bandera = 0
                            break
                if bandera == 0:
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    tarifa.IDRuta=get_object_or_404(Rutas, pk=form.cleaned_data["IDRuta"])
                    tarifa.Precio=form.cleaned_data["Precio"]
                    tarifa.ViajeRedondo=form.cleaned_data["ViajeRedondo"]
                    tarifa.IDTipoUnidad=get_object_or_404(TiposUnidades, pk=form.cleaned_data["IDTipoUnidad"])
                    tarifa.save()
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                data['bandera'] = 4
                return JsonResponse(data)

        context = {'form': form, 'actualizarTarifaG' : actualizarTarifaG, 'idT' : idT, 'idTa' : idTa}
        data['actualizarTarifaG'] = render_to_string('actualizarTarifaG.html', context, request=request)
        data['bandera'] = 1
        data['IDTransportista'] = idT
        data['IDRuta'] = tarifa.IDRuta.id
        data['IDTipoUnidad'] = tarifa.IDTipoUnidad.id
        data['Precio'] = tarifa.Precio
        data['ViajeRedondo'] = tarifa.ViajeRedondo
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectRutasActualizarG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        rutas = Rutas.objects.filter(Actividad = 1).order_by('NombreRuta').all()
        data['selectRutasActualizarG'] = render_to_string('selectRutasActualizarG.html', {'rutas': rutas, 'IDRuta' : datos['IDRuta']})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectTiposUnidadesTransportistaActualizarG(request):
    if (request.user.is_authenticated):
        request_data = request.POST
        datos = json.loads(request_data['data'])
        tiposUnidadesT=TransportistasProspectos.objects.filter(id=datos["IDTransportista"], Actividad = 1).order_by('RazonSocial').select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')

        arregloTiposUnidades = []
        for tipoUnidadT in tiposUnidadesT[0].IDTipoUnidad.all():
            arregloTiposUnidades.append(tipoUnidadT)
        
        data = dict()
        data['selectTiposUnidadesTransportistaActualizarG'] = render_to_string('selectTiposUnidadesTransportistaActualizarG.html',{'tiposUnidades' : arregloTiposUnidades, 'IDTipoUnidad' : datos['IDTipoUnidad']}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def buscarDatosRutaActualizarG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        ruta = Rutas.objects.filter(Actividad = 1, id=datos['idR']).all()
        data['CPOrigen'] = ruta[0].CPOrigen
        data['CiudadOrigen'] = ruta[0].CiudadOrigen
        data['EstadoOrigen'] = ruta[0].EstadoOrigen
        data['CPDestino'] = ruta[0].CPDestino
        data['CiudadDestino'] = ruta[0].CiudadDestino
        data['EstadoDestino'] = ruta[0].EstadoDestino
        data['Kilometros'] = ruta[0].Kilometros
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Borrar ruta en transportista
def borrarTarifaG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        tarifa = get_object_or_404(Tarifas, pk=datos['idTa'])
        tarifa.Actividad = 0
        tarifa.save()
        transportista = get_object_or_404(TransportistasProspectos, pk = datos['idT'])
        transportista.IDTarifa.remove(tarifa)
        transportista.save()
        data["bandera"] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')



#Asignar tipo unidad a transportista
def asignarTipoUnidadG(request, idT):
    if (request.user.is_authenticated):
        data = dict()
        asignarTipoUnidadG = "asignarTipoUnidadG/"+str(idT)+"/"
        form = TiposUnidadesForm()

        if (request.method == "POST"):
            transportista = get_object_or_404(TransportistasProspectos, pk=idT)
            form = TiposUnidadesForm(request.POST)
            if form.is_valid():
                transportista.IDTipoUnidad.add(get_object_or_404(TiposUnidades, pk=form.cleaned_data["Nombre"]))
                transportista.save()
                data['bandera'] = 2
                return JsonResponse(data)

        data['idT'] = idT
        context = {'form': form, 'asignarTipoUnidadG': asignarTipoUnidadG}
        data['asignarTipoUnidadG'] = render_to_string('asignarTipoUnidadG.html', context, request=request)
        data['bandera'] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectTiposUnidadesG(request):
    if (request.user.is_authenticated):
        request_data = request.POST
        datos = json.loads(request_data['data'])
        tiposUnidades = TiposUnidades.objects.filter(Actividad=1).order_by("Nombre").all()
        tiposUnidadesT = TransportistasProspectos.objects.filter(id=datos['idT'], Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')

        arregloTiposUnidades = []
        for tipoUnidad in tiposUnidades:
            bandera = 1
            for tipoUnidadT in tiposUnidadesT[0].IDTipoUnidad.order_by("Nombre").all():
                if tipoUnidad.Nombre == tipoUnidadT.Nombre:
                    bandera = 0 
                    break
            if bandera == 1:
                arregloTiposUnidades.append(tipoUnidad)

        data = dict()
        data['selectTiposUnidadesG'] = render_to_string('selectTiposUnidadesG.html',{'tiposUnidades' : arregloTiposUnidades}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Borrar el tipo de unidad en el transportista
def  borrarTipoUnidadG(request, idT, idU):
    if (request.user.is_authenticated):
        data = dict()
        borrarTipoUnidadG = "borrarTipoUnidadG/"+str(idT)+"/"+str(idU)+"/"
        form = TiposUnidadesForm()

        if (request.method == "POST"):
            form = TiposUnidadesForm(request.POST)
            transportista = get_object_or_404(TransportistasProspectos, pk=idT)
            if form.is_valid():
                bandera = 1
                tiposUnidadesT=TransportistasProspectos.objects.filter(id=idT, Actividad = 1).order_by('RazonSocial').select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
                for tipoUnidad in tiposUnidadesT[0].IDTarifa.all():
                    if tipoUnidad.IDTipoUnidad.id == idU:
                        bandera = 0
                        break

                if bandera == 1:
                    transportista.IDTipoUnidad.remove(get_object_or_404(TiposUnidades, pk=form.cleaned_data["Nombre"]))
                    transportista.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)

        context = {'form': form, 'borrarTipoUnidadG': borrarTipoUnidadG}
        data['borrarTipoUnidadG'] = render_to_string('borrarTipoUnidadG.html', context, request=request)
        data['idU'] = idU
        data['bandera'] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectTipoUnidadBorraG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        tipoUnidad = get_object_or_404(TiposUnidades, pk=datos["idU"])
        
        data['selectTipoUnidadBorraG'] = render_to_string('selectTipoUnidadBorraG.html',{'tipoUnidad' : tipoUnidad}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Agregar certificacion a transportista
def asignarCertificacionG(request, idT):
    if (request.user.is_authenticated):
        data = dict()
        asignarCertificacionG = "asignarCertificacionG/"+str(idT)+"/"
        form = CertificacionesForm()

        if (request.method == "POST"):
            transportista = get_object_or_404(TransportistasProspectos, pk=idT)
            form = CertificacionesForm(request.POST)
            if form.is_valid():
                transportista.IDCertificacion.add(get_object_or_404(Certificaciones, pk=form.cleaned_data["Nombre"]))
                transportista.save()
                data['bandera'] = 2
                return JsonResponse(data)

        context = {'form': form, 'asignarCertificacionG': asignarCertificacionG}
        data['asignarCertificacionG'] = render_to_string('asignarCertificacionG.html', context, request=request)
        data['idT'] = idT
        data['bandera'] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectCertificacionesG(request):
    if (request.user.is_authenticated):
        request_data = request.POST
        datos = json.loads(request_data['data'])
        certificaciones = Certificaciones.objects.filter(Actividad=1).order_by("Nombre").all()
        certificacionesT = TransportistasProspectos.objects.filter(id=datos['idT'], Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')

        arregloCertificaciones = []
        for certificacion in certificaciones:
            bandera = 1
            for certificacionT in certificacionesT[0].IDCertificacion.order_by("Nombre").all():
                if certificacion.Nombre == certificacionT.Nombre:
                    bandera = 0 
                    break
            if bandera == 1:
                arregloCertificaciones.append(certificacion)
                
        data = dict()
        data['selectCertificacionesG'] = render_to_string('selectCertificacionesG.html',{'certificaciones' : arregloCertificaciones}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Borrar certificacion a transportista
def borrarCertificacionG(request, idT, idC):
    if (request.user.is_authenticated):
        data = dict()
        borrarCertificacionG = "borrarCertificacionG/"+str(idT)+"/"+str(idC)+"/"
        form = CertificacionesForm()

        if (request.method == "POST"):
            form = CertificacionesForm(request.POST)
            transportista = get_object_or_404(TransportistasProspectos, pk=idT)
            if form.is_valid():
                transportista.IDCertificacion.remove(get_object_or_404(Certificaciones, pk=form.cleaned_data["Nombre"]))
                transportista.save()
                data['bandera'] = 2
                return JsonResponse(data)

        context = {'form': form, 'borrarCertificacionG': borrarCertificacionG}
        data['idC'] = idC
        data['bandera'] = 1
        data['borrarCertificacionG'] = render_to_string('borrarCertificacionG.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectCertificacionBorrarG(request):
    if (request.user.is_authenticated):
        request_data = request.POST
        datos = json.loads(request_data['data'])
        certificacion = get_object_or_404(Certificaciones, pk=datos["idC"])
        data = dict()
        data['selectCertificacionBorrarG'] = render_to_string('selectCertificacionBorrarG.html',{'certificacion' : certificacion}, request=request)
        data['bandera'] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')


 #Crear contacto a transportista
def crearContactoG(request, idT):
    if (request.user.is_authenticated):
        data = dict()
        form = ContactosForm()
        crearContactoG= "crearContactoG/"+str(idT)+"/"

        if request.method == "POST":
            form = ContactosForm(request.POST)
            if form.is_valid():
                bandera = 0
                transportista=TransportistasProspectos.objects.filter(id=idT, Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
                for contactoC in transportista[0].IDContacto.all():
                    if contactoC.Actividad==1:
                        if contactoC.Profesion == form.cleaned_data["Profesion"] and contactoC.NombreIFE == form.cleaned_data["NombreIFE"] and contactoC.PrimerNombre == form.cleaned_data["PrimerNombre"] and contactoC.SegundoNombre == form.cleaned_data["SegundoNombre"] and contactoC.ApellidoPaterno == form.cleaned_data["ApellidoPaterno"] and contactoC.ApellidoMaterno == form.cleaned_data["ApellidoMaterno"] and contactoC.Puesto == form.cleaned_data["Puesto"] and contactoC.Telefono == form.cleaned_data["Telefono"] and contactoC.Correo == form.cleaned_data["Correo"]:
                            bandera = 1
                            break
                if bandera == 0:
                    contacto = Contactos(
                        Profesion=form.cleaned_data["Profesion"],
                        NombreIFE=form.cleaned_data["NombreIFE"],
                        PrimerNombre=form.cleaned_data["PrimerNombre"],
                        SegundoNombre=form.cleaned_data["SegundoNombre"],
                        ApellidoPaterno=form.cleaned_data["ApellidoPaterno"],
                        ApellidoMaterno=form.cleaned_data["ApellidoMaterno"],
                        Puesto=form.cleaned_data["Puesto"],
                        Telefono=form.cleaned_data["Telefono"],
                        Correo=form.cleaned_data["Correo"],
                        CorreoAdicional=form.cleaned_data["CorreoAdicional"],
                    )
                    contacto.save()
                    transportista = get_object_or_404(TransportistasProspectos, pk=idT)
                    transportista.IDContacto.add(contacto)
                    transportista.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                data['bandera'] = 4
                return JsonResponse(data)

        context = {'form': form, 'crearContactoG': crearContactoG}
        data['crearContactoG'] = render_to_string('crearContactoG.html', context, request=request)
        data['bandera'] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Actualizar contacto a transportista
def actualizarContactoG(request, idT, idCO):
    if (request.user.is_authenticated):
        data = dict()
        contacto = get_object_or_404(Contactos, pk=idCO)
        form = ActualizarContactosForm(request.POST or None, instance=contacto)
        actualizarContactoG = "actualizarContactoG/"+str(idT)+"/"+str(idCO)+"/"
        if (request.method == "POST"):
            form = ContactosForm(request.POST)
            if form.is_valid():
                bandera = 0
                transportista=TransportistasProspectos.objects.filter(id=idT, Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
                for contactoC in transportista[0].IDContacto.all():
                    if contactoC.Actividad==1:
                        if contactoC.id != idCO:
                            if contactoC.Profesion == form.cleaned_data["Profesion"] and contactoC.NombreIFE == form.cleaned_data["NombreIFE"] and contactoC.PrimerNombre == form.cleaned_data["PrimerNombre"] and contactoC.SegundoNombre == form.cleaned_data["SegundoNombre"] and contactoC.ApellidoPaterno == form.cleaned_data["ApellidoPaterno"] and contactoC.ApellidoMaterno == form.cleaned_data["ApellidoMaterno"] and contactoC.Puesto == form.cleaned_data["Puesto"] and contactoC.Telefono == form.cleaned_data["Telefono"] and contactoC.Correo == form.cleaned_data["Correo"]:
                                bandera = 1
                                break
                if bandera == 0:
                    contacto.Profesion=form.cleaned_data["Profesion"]
                    contacto.NombreIFE=form.cleaned_data["NombreIFE"]
                    contacto.PrimerNombre=form.cleaned_data["PrimerNombre"]
                    contacto.SegundoNombre=form.cleaned_data["SegundoNombre"]
                    contacto.ApellidoPaterno=form.cleaned_data["ApellidoPaterno"]
                    contacto.ApellidoMaterno=form.cleaned_data["ApellidoMaterno"]
                    contacto.Puesto=form.cleaned_data["Puesto"]
                    contacto.Telefono=form.cleaned_data["Telefono"]
                    contacto.Correo=form.cleaned_data["Correo"]
                    contacto.CorreoAdicional=form.cleaned_data["CorreoAdicional"]
                    contacto.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                data['bandera'] = 4
                return JsonResponse(data)

        context = {'form': form, 'actualizarContactoG' : actualizarContactoG, 'idT' : idT, 'idCO' : idCO}
        data['actualizarContactoG'] = render_to_string('actualizarContactoG.html', context, request=request)
        data['bandera'] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

#Borrar contacto a transportista
def borrarContactoG(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        contacto = get_object_or_404(Contactos, pk=datos['idCO'])
        contacto.Actividad = 0
        contacto.save()
        transportista = get_object_or_404(TransportistasProspectos, pk=datos['idT'])
        transportista.IDContacto.remove(contacto)
        transportista.save()
        data["bandera"] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')



#Contactos
def contactos(request):
    if (request.user.is_authenticated):
        return render(request, "contactos.html")
    else:
        return HttpResponseRedirect('/')

def tablaContactos(request):
    if (request.user.is_authenticated):
        data = dict()
        contactos = Contactos.objects.filter(Actividad=1).order_by('NombreIFE').all()
        data['tablaContactos'] = render_to_string('tablaContactos.html', {'contactos': contactos}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def crearContacto(request):
    if (request.user.is_authenticated):
        data = dict()
        form = ContactosEnContactosForm()
        crearContacto= "crearContacto/"

        if request.method == "POST":
            form = ContactosEnContactosForm(request.POST)
            if form.is_valid():
                bandera = 0
                transportista=TransportistasProspectos.objects.filter(id=form.cleaned_data["IDTransportista"], Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
                for contactoC in transportista[0].IDContacto.all():
                    if contactoC.Actividad==1:
                        if contactoC.Profesion == form.cleaned_data["Profesion"] and contactoC.NombreIFE == form.cleaned_data["NombreIFE"] and contactoC.PrimerNombre == form.cleaned_data["PrimerNombre"] and contactoC.SegundoNombre == form.cleaned_data["SegundoNombre"] and contactoC.ApellidoPaterno == form.cleaned_data["ApellidoPaterno"] and contactoC.ApellidoMaterno == form.cleaned_data["ApellidoMaterno"] and contactoC.Puesto == form.cleaned_data["Puesto"] and int(contactoC.Telefono) == int(form.cleaned_data["Telefono"]) and contactoC.Correo == form.cleaned_data["Correo"]:
                            bandera = 1
                            break
                if bandera == 0:
                    contacto = Contactos(
                        Profesion=form.cleaned_data["Profesion"],
                        NombreIFE=form.cleaned_data["NombreIFE"],
                        PrimerNombre=form.cleaned_data["PrimerNombre"],
                        SegundoNombre=form.cleaned_data["SegundoNombre"],
                        ApellidoPaterno=form.cleaned_data["ApellidoPaterno"],
                        ApellidoMaterno=form.cleaned_data["ApellidoMaterno"],
                        Puesto=form.cleaned_data["Puesto"],
                        Telefono=form.cleaned_data["Telefono"],
                        Correo=form.cleaned_data["Correo"],
                        CorreoAdicional=form.cleaned_data["CorreoAdicional"],
                    )
                    contacto.save()
                    transportista = get_object_or_404(TransportistasProspectos, pk=form.cleaned_data["IDTransportista"])
                    transportista.IDContacto.add(contacto)
                    transportista.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)

            else:
                print(form.errors)
                data['bandera'] = 4
                return JsonResponse(data)

        data['bandera'] = 1
        context = {'form': form, 'crearContacto': crearContacto}
        data['crearContacto'] = render_to_string('crearContacto.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectTransportistasContactos(request):
    if (request.user.is_authenticated):
        data = dict()
        transportistas=TransportistasProspectos.objects.filter(Actividad=1).order_by('RazonSocial').select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
        data['selectTransportistasContactos'] = render_to_string('selectTransportistasContactos.html', {'transportistas': transportistas}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def actualizarContacto(request, idT, idCO):
    if (request.user.is_authenticated):
        data = dict()
        contacto = get_object_or_404(Contactos, pk=idCO)
        form = ActualizarContactosForm(request.POST or None, instance=contacto)
        actualizarContacto = "actualizarContacto/"+str(idT)+"/"+str(idCO)+"/"
        if (request.method == "POST"):
            form = ActualizarContactosForm(request.POST)
            if form.is_valid():
                bandera = 0
                transportista=TransportistasProspectos.objects.filter(id=idT, Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
                for contactoC in transportista[0].IDContacto.all():
                    if contactoC.Actividad==1:
                        if contactoC.id != idCO:
                            if contactoC.Profesion == form.cleaned_data["Profesion"] and contactoC.NombreIFE == form.cleaned_data["NombreIFE"] and contactoC.PrimerNombre == form.cleaned_data["PrimerNombre"] and contactoC.SegundoNombre == form.cleaned_data["SegundoNombre"] and contactoC.ApellidoPaterno == form.cleaned_data["ApellidoPaterno"] and contactoC.ApellidoMaterno == form.cleaned_data["ApellidoMaterno"] and contactoC.Puesto == form.cleaned_data["Puesto"] and contactoC.Telefono == form.cleaned_data["Telefono"] and contactoC.Correo == form.cleaned_data["Correo"]:
                                bandera = 1
                                break
                if bandera == 0:
                    contacto.Profesion=form.cleaned_data["Profesion"]
                    contacto.NombreIFE=form.cleaned_data["NombreIFE"]
                    contacto.PrimerNombre=form.cleaned_data["PrimerNombre"]
                    contacto.SegundoNombre=form.cleaned_data["SegundoNombre"]
                    contacto.ApellidoPaterno=form.cleaned_data["ApellidoPaterno"]
                    contacto.ApellidoMaterno=form.cleaned_data["ApellidoMaterno"]
                    contacto.Puesto=form.cleaned_data["Puesto"]
                    contacto.Telefono=form.cleaned_data["Telefono"]
                    contacto.Correo=form.cleaned_data["Correo"]
                    contacto.CorreoAdicional=form.cleaned_data["CorreoAdicional"]
                    contacto.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                data['bandera'] = 4
                return JsonResponse(data)

        data['bandera'] = 1
        context = {'form': form, 'actualizarContacto' : actualizarContacto, 'idT' : idT, 'idCO' : idCO}
        data['actualizarContacto'] = render_to_string('actualizarContacto.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def borrarContacto(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])
        contacto = get_object_or_404(Contactos, pk=datos['idCO'])
        contacto.Actividad = 0
        contacto.save()
        transportista = get_object_or_404(TransportistasProspectos, pk=datos['idT'])
        transportista.IDContacto.remove(contacto)
        transportista.save()
        data["bandera"] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')



#Tipos de Unidad
def tiposUnidades(request):
    if (request.user.is_authenticated):
        return render(request, "tiposUnidades.html")
    else:
        return HttpResponseRedirect('/')

def tablaTiposUnidades(request):
    if (request.user.is_authenticated):
        data = dict()
        tiposUnidades = TiposUnidades.objects.filter(Actividad=1).order_by('Nombre').all()
        data['tablaTiposUnidades'] = render_to_string('tablaTiposUnidades.html', {'tiposUnidades': tiposUnidades}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def crearTipoUnidad(request):
    if (request.user.is_authenticated):
        data = dict()
        form = TipoUnidadesEnTiposUnidadesForm()
        crearTipoUnidad = "crearTipoUnidad/"
        if (request.method == "POST"):
            form = TipoUnidadesEnTiposUnidadesForm(request.POST)
            if form.is_valid():
                if TiposUnidades.objects.filter(Nombre = form.cleaned_data["Nombre"], IDCategoriaEje = form.cleaned_data["IDCategoriaEje"], Actividad = 1).exists()==False:
                    tipoUnidad = TiposUnidades(
                        Nombre=form.cleaned_data["Nombre"],
                        VolumenMax=form.cleaned_data["VolumenMax"],
                        PesoMax=form.cleaned_data["PesoMax"],
                        Ancho=form.cleaned_data["Ancho"],
                        Largo=form.cleaned_data["Largo"],
                        IDCategoriaEje=get_object_or_404(CategoriasEjes, pk=form.cleaned_data["IDCategoriaEje"]),
                    )
                    tipoUnidad.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                print(form.errors)
                data['bandera'] = 4
                return JsonResponse(data)

        context = {'form': form, 'crearTipoUnidad' : crearTipoUnidad}
        data['bandera'] = 1
        data['crearTipoUnidad'] = render_to_string('crearTipoUnidad.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectCategoriasEjes(request):
    if (request.user.is_authenticated):
        categoriasEjes = CategoriasEjes.objects.filter(Actividad = 1).order_by('Nombre').all()
        data = dict()
        data['selectCategoriasEjes'] = render_to_string('selectCategoriasEjes.html', {'categoriasEjes': categoriasEjes}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def actualizarTipoUnidad(request, idTU):
    if (request.user.is_authenticated):
        data = dict()
        tipoUnidad = get_object_or_404(TiposUnidades, pk=idTU)
        form = ActualizarTipoUnidadesEnTiposUnidadesForm(request.POST or None, instance=tipoUnidad)
        actualizarTipoUnidad = "actualizarTipoUnidad/"+str(idTU)+"/"

        if (request.method == "POST"):
            form = TipoUnidadesEnTiposUnidadesForm(request.POST)
            if form.is_valid():
                if TiposUnidades.objects.filter(~Q(id=idTU)).filter(Nombre=form.cleaned_data["Nombre"], IDCategoriaEje=form.cleaned_data["IDCategoriaEje"], Actividad=1).exists()==False:
                    tipoUnidad.Nombre=form.cleaned_data["Nombre"]
                    tipoUnidad.VolumenMax=form.cleaned_data["VolumenMax"]
                    tipoUnidad.PesoMax=form.cleaned_data["PesoMax"]
                    tipoUnidad.Ancho=form.cleaned_data["Ancho"]
                    tipoUnidad.Largo=form.cleaned_data["Largo"]
                    tipoUnidad.IDCategoriaEje=get_object_or_404(CategoriasEjes, pk=form.cleaned_data["IDCategoriaEje"])
                    tipoUnidad.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                print(form.errors)
                data['bandera'] = 4
                return JsonResponse(data)

        data['idCE'] = tipoUnidad.IDCategoriaEje.id
        data['bandera'] = 1
        context = {'form': form, 'actualizarTipoUnidad' : actualizarTipoUnidad, 'idTU' : idTU}
        data['actualizarTipoUnidad'] = render_to_string('actualizarTipoUnidad.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def selectActualizarTipoUnidad(request):
    if (request.user.is_authenticated):
        request_data = request.POST
        datos = json.loads(request_data['data'])
        categoriasEjes = CategoriasEjes.objects.filter(Actividad=1).order_by('Nombre').all()
        data = dict()
        data['selectActualizarTipoUnidad'] = render_to_string('selectActualizarTipoUnidad.html', {'categoriasEjes': categoriasEjes, 'idCE' : datos['idCE']}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def borrarTipoUnidad(request):
    if (request.user.is_authenticated):
        request_data = request.POST
        datos = json.loads(request_data['data'])
        data = dict()
        bandera = 1

        transportistas=TransportistasProspectos.objects.filter(Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
        BTipoUnidad = get_object_or_404(TiposUnidades, pk=datos["idTU"])
        for transportista in  transportistas:
            for TipoUnidad in transportista.IDTipoUnidad.all():
                if TipoUnidad.id == BTipoUnidad.id:
                    bandera = 0
                    break
            if bandera == 0:
                break

        costeos = Costeo.objects.filter(Actividad = 1).select_related('IDDepreciacion').select_related('IDRuta').select_related('IDFactoresPremisas').select_related('IDCostosOperativos').all()
        BTipoUnidad = get_object_or_404(TiposUnidades, pk=datos["idTU"])
        for costeo in  costeos:
            if costeo.IDTipoUnidad.id == BTipoUnidad.id:
                bandera = 0
                break
    
        if bandera == 1:
            BTipoUnidad.Actividad = 0
            BTipoUnidad.save()
            data["bandera"] = 1
            return JsonResponse(data)
        else:
            BTipoUnidad.Actividad = 1
            BTipoUnidad.save()
            data["bandera"] = 2
            return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')



#Certificaciones
def certificaciones(request):
    if (request.user.is_authenticated):
        return render(request, "certificaciones.html")
    else:
        return HttpResponseRedirect('/')

def tablaCertificaciones(request):
    if (request.user.is_authenticated):
        data = dict()
        certificaciones = Certificaciones.objects.filter(Actividad=1).order_by('Nombre').all()
        data['tablaCertificaciones'] = render_to_string('tablaCertificaciones.html', {'certificaciones': certificaciones}, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def crearCertificacion(request):
    if (request.user.is_authenticated):
        data = dict()
        form = CertificacionesEnCertificacionesForm()
        crearCertificacion = "crearCertificacion/"
        if (request.method == "POST"):
            form = CertificacionesEnCertificacionesForm(request.POST)
            if form.is_valid():
                if Certificaciones.objects.filter(Nombre=form.cleaned_data["Nombre"], Actividad=1).exists()==False:
                    certificacion = Certificaciones(
                        Nombre=form.cleaned_data["Nombre"],
                    )
                    certificacion.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                print(form.errors)
                data['bandera'] = 4
                return JsonResponse(data)

        data['bandera'] = 1
        context = {'form': form, 'crearCertificacion' : crearCertificacion}
        data['crearCertificacion'] = render_to_string('crearCertificacion.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def actualizarCertificacion(request, idCer):
    if (request.user.is_authenticated):
        data = dict()
        certificacion = get_object_or_404(Certificaciones, pk=idCer)
        form = ActualizarCertificacionesEnCertificacionesForm(request.POST or None, instance=certificacion)
        actualizarCertificacion = "actualizarCertificacion/"+str(idCer)+"/"

        if (request.method == "POST"):
            form = CertificacionesEnCertificacionesForm(request.POST)
            if form.is_valid():
                if Certificaciones.objects.filter(~Q(id=idCer)).filter(Nombre=form.cleaned_data["Nombre"], Actividad=1).exists()==False:
                    certificacion.Nombre=form.cleaned_data["Nombre"]
                    certificacion.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                print(form.errors)
                data['bandera'] = 4
                return JsonResponse(data)
        
        data['bandera'] = 1
        context = {'form': form, 'actualizarCertificacion' : actualizarCertificacion, 'idCer' : idCer}
        data['actualizarCertificacion'] = render_to_string('actualizarCertificacion.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def borrarCertificacion(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])

        transportistas=TransportistasProspectos.objects.filter(Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
        Bcertificacion = get_object_or_404(Certificaciones, pk=datos["idCer"])
        for transportista in  transportistas:
            for certificacion in transportista.IDCertificacion.all():
                if certificacion.id == Bcertificacion.id:
                    Bcertificacion.Actividad = 1
                    Bcertificacion.save()
                    data["bandera"] = 2
                    return JsonResponse(data)

        Bcertificacion.Actividad = 0
        Bcertificacion.save()
        data["bandera"] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')