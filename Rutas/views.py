from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Rutas, TiposUnidades
from TransportistasProspecto.models import TransportistasProspectos
from Costeo.models import Costeo
#from Rutas.forms import RutasForm, CrearRutasForm, ActualizarRutasForm
from Rutas.forms import CrearRutasTForm, ActualizarRutasTForm
from django.db.models import Q
import json
import requests


def rutasT(request):
    if (request.user.is_authenticated):
        return render(request, "rutasT.html")
    else:
        return HttpResponseRedirect('/')

def tablaRutasT(request):
    if (request.user.is_authenticated):
        data = dict()
        rutas=Rutas.objects.filter(Actividad = 1).order_by('NombreRuta').all()
        data['tablaRutasT'] = render_to_string('tablaRutasT.html', {'rutas': rutas})
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def crearRutaT(request):
    if (request.user.is_authenticated):
        data = dict()
        crearRutaT="crearRutaT/"
        form = CrearRutasTForm()

        if request.method == "POST":
            form = CrearRutasTForm(request.POST)
            if form.is_valid():
                bandera = 1
                rutas = Rutas.objects.filter(Actividad = 1).all()
                for ruta in rutas:
                    if ruta.NombreRuta == form.cleaned_data["NombreRuta"] and ruta.CPOrigen == form.cleaned_data["CPOrigen"] and ruta.CiudadOrigen == form.cleaned_data["CiudadOrigen"] and ruta.EstadoOrigen == form.cleaned_data["EstadoOrigen"] and ruta.CPDestino == form.cleaned_data["CPDestino"] and ruta.CiudadDestino == form.cleaned_data["CiudadDestino"] and ruta.EstadoDestino == form.cleaned_data["EstadoDestino"] and ruta.Kilometros == form.cleaned_data["Kilometros"]:
                        bandera = 0
                        break
                if bandera == 1:
                    ruta = Rutas(
                        NombreRuta=form.cleaned_data["NombreRuta"],
                        CPOrigen=form.cleaned_data["CPOrigen"],
                        CiudadOrigen=form.cleaned_data["CiudadOrigen"],
                        EstadoOrigen=form.cleaned_data["EstadoOrigen"],
                        CPDestino=form.cleaned_data["CPDestino"],
                        CiudadDestino=form.cleaned_data["CiudadDestino"],
                        EstadoDestino=form.cleaned_data["EstadoDestino"],
                        Kilometros=form.cleaned_data["Kilometros"],
                    )
                    ruta.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                data['bandera'] = 4
                return JsonResponse(data)

        data['bandera'] = 1
        context = {'form': form, 'crearRutaT':crearRutaT }
        data['crearRutaT'] = render_to_string('crearRutaT.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def actualizarRutaT(request, idR):
    if (request.user.is_authenticated):
        data = dict()
        ruta = get_object_or_404(Rutas, pk=idR)
        form = ActualizarRutasTForm(request.POST or None, instance=ruta)
        actualizarRutaT = "actualizarRutaT/"+str(idR)+"/"

        if (request.method == "POST"):
            form = CrearRutasTForm(request.POST)
            if form.is_valid():
                bandera = 1
                rutas = Rutas.objects.filter(~Q(id=idR),Actividad=1).all()
                for rutaC in rutas:
                    if rutaC.NombreRuta == form.cleaned_data["NombreRuta"] and rutaC.CPOrigen == form.cleaned_data["CPOrigen"] and rutaC.CiudadOrigen == form.cleaned_data["CiudadOrigen"] and rutaC.EstadoOrigen == form.cleaned_data["EstadoOrigen"] and rutaC.CPDestino == form.cleaned_data["CPDestino"] and rutaC.CiudadDestino == form.cleaned_data["CiudadDestino"] and rutaC.EstadoDestino == form.cleaned_data["EstadoDestino"] and rutaC.Kilometros == form.cleaned_data["Kilometros"]:
                        bandera = 0
                        break
                if bandera == 1:
                    ruta.NombreRuta=form.cleaned_data["NombreRuta"]
                    ruta.CPOrigen=form.cleaned_data["CPOrigen"]
                    ruta.CiudadOrigen=form.cleaned_data["CiudadOrigen"]
                    ruta.EstadoOrigen=form.cleaned_data["EstadoOrigen"]
                    ruta.CPDestino=form.cleaned_data["CPDestino"]
                    ruta.CiudadDestino=form.cleaned_data["CiudadDestino"]
                    ruta.EstadoDestino=form.cleaned_data["EstadoDestino"]
                    ruta.Kilometros=form.cleaned_data["Kilometros"]
                    ruta.save()
                    data['bandera'] = 2
                    return JsonResponse(data)
                else:
                    data['bandera'] = 3
                    return JsonResponse(data)
            else:
                data['bandera'] = 4
                return JsonResponse(data)

        data['bandera'] = 1
        context = {'form': form, 'actualizarRutaT' : actualizarRutaT, 'idR' : idR}
        data['actualizarRutaT'] = render_to_string('actualizarRutaT.html', context, request=request)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def IdCdRuta(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])

        url = 'http://gaia.inegi.org.mx/sakbe_v3.1/buscadestino' 
        params = {'type': "json",'buscar':datos['ciudad'], 'proj': "MERC",'num':50,'key': "x4cGBaOC-423Z-A9ii-AKwM-QWiCfq63rMu9"}
        r = requests.post(url, params=params)
        resjson = r.json()
        for val in resjson['data']:
            string=val['ent_abr'].replace(".","")
            string=string.replace(" ","")
            if comparaestadosRuta(string)==datos['estado']:
                data["cod"] = val['id_dest']
                data["bandera"] = 2
                return JsonResponse(data)

        palabras = datos['ciudad'].split()
        for palabra in palabras:
            url = 'http://gaia.inegi.org.mx/sakbe_v3.1/buscadestino' 
            params = {'type': "json",'buscar':palabra, 'proj': "MERC",'num':50,'key': "x4cGBaOC-423Z-A9ii-AKwM-QWiCfq63rMu9"}
            r = requests.post(url, params=params)
            resjson = r.json()
            for val in resjson['data']:
                string=val['ent_abr'].replace(".","")
                string=string.replace(" ","")
                if comparaestadosRuta(string)==datos['estado']:
                    data["cod"] = val['id_dest']
                    data["bandera"] = 2
                    return JsonResponse(data)

        data["bandera"] = 1
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')

def comparaestadosRuta(argument):
    switcher = {
        "Ags":"Aguascalientes",
        "BC":"Baja California",
        "BCS":"Baja California Sur",
        "Camp":"Campeche",
        "Coah":"Coahuila de Zaragoza",
        "Col":"Colima",
        "Chis":"Chiapas",
        "Chih":"Chihuahua",
        "CDMX":"Ciudad de México",
        "Dgo":"Durango",
        "Gto":"Guanajuato",
        "Gro":"Guerrero",
        "Hgo":"Hidalgo",
        "Jal":"Jalisco",
        "Mex":"México",
        "Mich":"Michoacán de Ocampo",
        "Mor":"Morelos",
        "Nay":"Nayarit",
        "NL":"Nuevo León",
        "Oax":"Oaxaca",
        "Pue":"Puebla",
        "Qro":"Querétaro",
        "QRoo":"Quintana Roo",
        "SLP":"San Luis Potosí",
        "Sin":"Sinaloa",
        "Son":"Sonora",
        "Tab":"Tabasco",
        "Tamps":"Tamaulipas",
        "Tlax":"Tlaxcala",
        "Ver":"Veracruz de Ignacio de la Llave",
        "Yuc":"Yucatán",
        "Zac":"Zacatecas",
    }
    return switcher.get(argument, "nothing")

def borrarRutaT(request):
    if (request.user.is_authenticated):
        data = dict()
        request_data = request.POST
        datos = json.loads(request_data['data'])

        bandera = 1
        transportistasR=TransportistasProspectos.objects.filter(Actividad = 1).select_related('IDPrioridad').select_related('IDEstatus').prefetch_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDTarifa').prefetch_related('IDContacto')
        costeosR = Costeo.objects.filter(Actividad = 1).select_related('IDDepreciacion').select_related('IDRuta').select_related('IDFactoresPremisas').select_related('IDCostosOperativos').all()

        for transportistaR in transportistasR:
            for rutaR in transportistaR.IDTarifa.all():
                if int(rutaR.IDRuta.id) == int(datos['idR']):
                    bandera = 0
                    break
            if bandera == 0:
                break
        
        for costeoR in costeosR:
            if int(costeoR.IDRuta.id) == int(datos['idR']):
                bandera = 0
                break

        if bandera == 1:
            ruta = get_object_or_404(Rutas, pk=datos['idR'])
            ruta.Actividad = 0
            ruta.save()
            data["bandera"] = 1
            return JsonResponse(data)
        else:
            data["bandera"] = 2
            return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')


"""
def rutas(request):
    return render(request, "rutas.html")

def tablaRutas(request):
    data = dict()
    rutas=Rutas.objects.filter(Actividad = 1).order_by('NombreRuta').all()
    data['tablaRutas'] = render_to_string('tablaRutas.html', {'rutas': rutas})
    return JsonResponse(data)

def crearRuta(request):
    data = dict()
    crearRuta="crearRuta/"
    form = CrearRutasForm()

    if request.method == "POST":
        form = CrearRutasForm(request.POST)
        if form.is_valid():
            bandera = 1
            rutas = TransportistasProspectos.objects.filter(id=form.cleaned_data["IDTransportista"], Actividad = 1).select_related('IDPrioridad').select_related('IDEstatus').select_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDRuta').prefetch_related('IDContacto')
            for ruta in rutas[0].IDRuta.all():
                if ruta.NombreRuta == form.cleaned_data["NombreRuta"] and ruta.CPOrigen == form.cleaned_data["CPOrigen"] and ruta.CiudadOrigen == form.cleaned_data["CiudadOrigen"] and ruta.EstadoOrigen == form.cleaned_data["EstadoOrigen"] and ruta.CPDestino == form.cleaned_data["CPDestino"] and ruta.CiudadDestino == form.cleaned_data["CiudadDestino"] and ruta.EstadoDestino == form.cleaned_data["EstadoDestino"] and ruta.Kilometros == form.cleaned_data["Kilometros"] and ruta.Precio == form.cleaned_data["Precio"] and ruta.ViajeRedondo == form.cleaned_data["ViajeRedondo"] and ruta.IDTipoUnidad.id == int(form.cleaned_data["IDTipoUnidad"]):
                    bandera = 0
                    break
            if bandera == 1:
                transportista = get_object_or_404(TransportistasProspectos, pk=form.cleaned_data["IDTransportista"])
                ruta = Rutas(
                    NombreRuta=form.cleaned_data["NombreRuta"],
                    CPOrigen=form.cleaned_data["CPOrigen"],
                    CiudadOrigen=form.cleaned_data["CiudadOrigen"],
                    EstadoOrigen=form.cleaned_data["EstadoOrigen"],
                    CPDestino=form.cleaned_data["CPDestino"],
                    CiudadDestino=form.cleaned_data["CiudadDestino"],
                    EstadoDestino=form.cleaned_data["EstadoDestino"],
                    Kilometros=form.cleaned_data["Kilometros"],
                    Precio=form.cleaned_data["Precio"],
                    ViajeRedondo=form.cleaned_data["ViajeRedondo"],
                    IDTipoUnidad=get_object_or_404(TiposUnidades, pk=form.cleaned_data["IDTipoUnidad"]),
                )
                ruta.save()
                transportista.IDRuta.add(ruta)
                transportista.save()
                data['bandera'] = 2
                return JsonResponse(data)
            else:
                data['bandera'] = 3
                return JsonResponse(data)
        else:
            data['bandera'] = 4
            return JsonResponse(data)

    data['bandera'] = 1
    context = {'form': form, 'crearRuta':crearRuta }
    data['crearRuta'] = render_to_string('crearRuta.html', context, request=request)
    return JsonResponse(data)

def selectTransportistasRutas(request):
    data = dict()
    transportistas=TransportistasProspectos.objects.filter(Actividad=1).order_by('RazonSocial').select_related('IDPrioridad').select_related('IDEstatus').select_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDRuta').prefetch_related('IDContacto')
    data['selectTransportistasRutas'] = render_to_string('selectTransportistasRutas.html', {'transportistas': transportistas})
    return JsonResponse(data)

def selectTiposUnidadesTransportista(request):
    data = dict()
    request_data = request.POST
    datos = json.loads(request_data['data'])
    tiposUnidadesT = TransportistasProspectos.objects.filter(id=datos['idT'], Actividad = 1).select_related('IDPrioridad').select_related('IDEstatus').select_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDRuta').prefetch_related('IDContacto')

    arregloTiposUnidades = []
    for tipoUnidadT in tiposUnidadesT[0].IDTipoUnidad.order_by('Nombre').all():
        arregloTiposUnidades.append(tipoUnidadT)
            
    data['selectTiposUnidadesTransportista'] = render_to_string('selectTiposUnidadesTransportista.html',{'tiposUnidades' : arregloTiposUnidades}, request=request)
    return JsonResponse(data)

def actualizarRuta(request, idT, idR):
    data = dict()
    ruta = get_object_or_404(Rutas, pk=idR)
    form = ActualizarRutasForm(request.POST or None, instance=ruta)
    actualizarRuta = "actualizarRuta/"+str(idT)+"/"+str(idR)+"/"

    if (request.method == "POST"):
        form = RutasForm(request.POST)
        if form.is_valid():
            bandera = 1
            rutas = TransportistasProspectos.objects.filter(id=idT, Actividad = 1).select_related('IDPrioridad').select_related('IDEstatus').select_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDRuta').prefetch_related('IDContacto')
            for ruta in rutas[0].IDRuta.all():
                if ruta.id != idR:
                    if ruta.NombreRuta == form.cleaned_data["NombreRuta"] and ruta.CPOrigen == form.cleaned_data["CPOrigen"] and ruta.CiudadOrigen == form.cleaned_data["CiudadOrigen"] and ruta.EstadoOrigen == form.cleaned_data["EstadoOrigen"] and ruta.CPDestino == form.cleaned_data["CPDestino"] and ruta.CiudadDestino == form.cleaned_data["CiudadDestino"] and ruta.EstadoDestino == form.cleaned_data["EstadoDestino"] and ruta.Kilometros == form.cleaned_data["Kilometros"] and ruta.Precio == form.cleaned_data["Precio"] and ruta.ViajeRedondo == form.cleaned_data["ViajeRedondo"] and ruta.IDTipoUnidad.id == int(form.cleaned_data["IDTipoUnidad"]):
                        bandera = 0
                        break
            if bandera == 1:
                ruta.NombreRuta=form.cleaned_data["NombreRuta"]
                ruta.CPOrigen=form.cleaned_data["CPOrigen"]
                ruta.CiudadOrigen=form.cleaned_data["CiudadOrigen"]
                ruta.EstadoOrigen=form.cleaned_data["EstadoOrigen"]
                ruta.CPDestino=form.cleaned_data["CPDestino"]
                ruta.CiudadDestino=form.cleaned_data["CiudadDestino"]
                ruta.EstadoDestino=form.cleaned_data["EstadoDestino"]
                ruta.Kilometros=form.cleaned_data["Kilometros"]
                ruta.Precio=form.cleaned_data["Precio"]
                ruta.ViajeRedondo=form.cleaned_data["ViajeRedondo"]
                ruta.IDTipoUnidad=get_object_or_404(TiposUnidades, pk=form.cleaned_data["IDTipoUnidad"])
                ruta.save()
                data['bandera'] = 2
                return JsonResponse(data)
            else:
                data['bandera'] = 3
                return JsonResponse(data)
        else:
            data['bandera'] = 4
            return JsonResponse(data)

    
    data['idT'] = idT
    data['idTU'] = ruta.IDTipoUnidad.id
    data['bandera'] = 1
    context = {'form': form, 'actualizarRuta' : actualizarRuta, 'idT' : idT, 'idR' : idR}
    data['actualizarRuta'] = render_to_string('actualizarRuta.html', context, request=request)
    return JsonResponse(data)

def selectTipoUnidadActualizar(request):
    data = dict()
    request_data = request.POST
    datos = json.loads(request_data['data'])
    tiposUnidadesT = TransportistasProspectos.objects.filter(id=datos['idT'], Actividad=1).select_related('IDPrioridad').select_related('IDEstatus').select_related('IDTipo').prefetch_related('IDTipoUnidad').prefetch_related('IDCertificacion').prefetch_related('IDRuta').prefetch_related('IDContacto')

    arregloTiposUnidades = []
    for tipoUnidadT in tiposUnidadesT[0].IDTipoUnidad.order_by('Nombre').all():
        arregloTiposUnidades.append(tipoUnidadT)

    context = {'tiposUnidades' : arregloTiposUnidades, 'idTU' : datos['idTU']}
    data['selectTipoUnidadActualizar'] = render_to_string('selectTipoUnidadActualizar.html',context, request=request)
    return JsonResponse(data)

def borrarRuta(request):
    data = dict()
    request_data = request.POST
    datos = json.loads(request_data['data'])
    ruta = get_object_or_404(Rutas, pk=datos['idR'])
    ruta.Actividad = 0
    ruta.save()
    transportista = get_object_or_404(TransportistasProspectos, pk=datos['idT'])
    transportista.IDRuta.remove(ruta)
    transportista.save()
    data["bandera"] = 1
    return JsonResponse(data)
"""