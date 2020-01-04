from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from Costeo.models import Depreciacion, FactoresPremisas, CostosOperativos, Costeo, Cotizacion
from Costeo.forms import CosteoForm, CotizacionForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import forms
from Transportista import models as carrier_models
from django.template.loader import render_to_string
from urllib.request import urlopen
import xmltodict
import json
from django.contrib.auth.decorators import login_required
@login_required
def firstTime(request):
    depreciacion = Depreciacion(
                Meses = 60,
                CostosUnidad = 800000.00,
                CostosCaja = 90000.00,
                ViajesMes=1,
                KmsMesXunidad = 14000,
                KmsMaximo = 15000,
                DepTracto = .95,
                DepCaja = .11,
                RentaGPS = 400.00,
                PlacasTenencia = 3000.00,
                Seguro = 10000.00,
                Admvo = 4,
                Financieros = 2,
                MttoUnidadXkm = 1.3,
                Llantas = .3,
                Operador = 1.3,
                DobleOp = 1.3
                )
    depreciacion.save()

    factoresPremisas = FactoresPremisas(
                Unidad = 1,
                Caja = 1,
                KmSencillo = 1169.00,
                KmRoundTrip = 0,
                KmMensuales = 0,
                CasetaSingle = 3996,
                Rendimiento = 2.8,
                Diesel = 21.80,
                DieselSinIva = 18.31,
                )
    factoresPremisas.save()

    
    costosOperativos = CostosOperativos(
                Combustible = 7645.00,
                Casetas = 3445.00,
                Operador = 1520.00,
                Subtotal1 = 12610.00,
                MttoUnidad = 1520.00,
                LlantasUnidad = 351.00,
                Gps = 31.00,
                Seguro = 779.00,
                PlacasTenencia = 234.00,
                SubTotal2 = 2915.00,
                Admvo = 621.00,
                Financieros = 310.00,
                DeprUnidad = 1113.00,
                DeprRemolque = 125.00,
                Subtotal3 = 2170.00,
                )
    costosOperativos.save()

# Create your views here.
@login_required
def Home(request):
    if request.user.is_authenticated:
        costeo = Costeo.objects.all().select_related('IDDepreciacion').select_related('IDRuta').select_related('IDFactoresPremisas').select_related('IDCostosOperativos').select_related('IDUnidad')
        context = {
            "costeo": costeo,
        }
        return render(request, "costeoHome.html", context)
    else:
        return HttpResponseRedirect('/')


def loadTransport(request):
    transport = carrier_models.Transportista.objects.all()
    serialized_queryset = serializers.serialize('python', transport)
    return JsonResponse(serialized_queryset, safe=False)

def loadUnidades(request):
    unidad = carrier_models.Unidad.objects.all()
    serialized_queryset = serializers.serialize('python', unidad)
    return JsonResponse(serialized_queryset, safe=False)


def loadRutas(request, id):
    rutas = "";
    if carrier_models.Transportista.objects.filter(pk=id).exists():
        carrier = carrier_models.Transportista.objects.get(pk=id)
        rutas = carrier.IDRutas.all()
    serialized_queryset = serializers.serialize('python', rutas)
    return JsonResponse(serialized_queryset, safe=False)


def getRuta(request, id):
    rutas = "";
    if carrier_models.rutas_models.Rutas.objects.filter(pk=id).exists():
        rutas = carrier_models.rutas_models.Rutas.objects.filter(pk=id).all()
        print(rutas)
    serialized_queryset = serializers.serialize('python', rutas)
    return JsonResponse(serialized_queryset, safe=False)

@login_required
def costeos(request):
    if request.user.is_authenticated:
        depreciacion = get_object_or_404(Depreciacion, pk=1)
        factoresPremisas = get_object_or_404(FactoresPremisas, pk=1)


        file = urlopen('https://publicacionexterna.azurewebsites.net/publicaciones/prices')
        data = file.read()
        file.close()
        MaxDiesel=0
        count=0
        data = xmltodict.parse(data)
        for Combustible in data['places']['place'] :
            for precios in Combustible['gas_price']:
                if isinstance(precios, str) is False:
                    if (precios['@type']) == 'diesel':
                        PrecioMax=float(precios['#text'])
                        MaxDiesel+=PrecioMax
                        count+=1

        
        costeo = Costeo.objects.all()
        MaxDiesel=MaxDiesel/count
        MaxDiesel=round(MaxDiesel,2)
        factoresPremisas.Diesel=MaxDiesel
        factoresPremisas.DieselSinIva=round(MaxDiesel/1.16,2)
        form = CosteoForm()
        if request.method == "POST":

            form = CosteoForm(request.POST)
            if form.is_valid():
                depreciacion = Depreciacion(
                    Meses=request.POST['mesesId'],
                    CostosUnidad=request.POST['costosUnidadId'],
                    CostosCaja=request.POST['costosCajaId'],
                    ViajesMes=request.POST['viajesMesId'],
                    KmsMesXunidad=request.POST['kmsMesXunidadId'],
                    KmsMaximo=request.POST['kmsMaximoId'],
                    DepTracto=request.POST['depTractoId'],
                    DepCaja=request.POST['depCajaId'],
                    RentaGPS=request.POST['rentaGPSId'],
                    PlacasTenencia=request.POST['placasTenenciaId'],
                    Seguro=request.POST['seguroId'],
                    Admvo=request.POST['admvoId'],
                    Financieros=request.POST['financierosId'],
                    MttoUnidadXkm=request.POST['mttoUnidadXkmId'],
                    Llantas=request.POST['llantasId'],
                    Operador=request.POST['operadorId'],
                    DobleOp=request.POST['dobleOpId']
                )
                depreciacion.save()
                factoresPremisas = FactoresPremisas(
                    Unidad=request.POST['unidadId'],
                    Caja=1,
                    KmSencillo=request.POST['kmSencilloId'],
                    KmRoundTrip=request.POST['kmRoundTripId'],
                    KmMensuales=request.POST['kmMensualesId'],
                    CasetaSingle=request.POST['casetaSingleId'],
                    Rendimiento=request.POST['rendimientoId'],
                    Diesel=request.POST['dieselId'],
                    DieselSinIva=request.POST['dieselSinIvaId'],

                )
                factoresPremisas.save()
                costosOperativos = CostosOperativos(
                    Combustible=request.POST['CombustibleId'],
                    Casetas=request.POST['CasetasId'],
                    Operador=request.POST['OperadorId'],
                    Subtotal1=request.POST['SubTotalId'],
                    MttoUnidad=request.POST['MttoUnidadId'],
                    LlantasUnidad=request.POST['LlantasUnidadId'],
                    Gps=request.POST['GPSId'],
                    Seguro=request.POST['SeguroId'],
                    PlacasTenencia=request.POST['PlacasTenenciaCostId'],
                    SubTotal2=request.POST['SubTotal2Id'],
                    Admvo=request.POST['AdmvoId'],
                    Financieros=request.POST['FinancierosId'],
                    DeprUnidad=request.POST['DeprUnidadId'],
                    DeprRemolque=request.POST['DeprRemolqueId'],
                    Subtotal3=request.POST['SubTotal3Id']
                )
                costosOperativos.save()
                costeo = Costeo(
                    IDTransportista=get_object_or_404(carrier_models.Transportista,
                                                      pk=form.cleaned_data["IDTransportista"]),
                    IDRuta=get_object_or_404(carrier_models.rutas_models.Rutas, pk=form.cleaned_data["IDRuta"]),
                    IDDepreciacion=depreciacion,
                    IDFactoresPremisas=factoresPremisas,
                    IDCostosOperativos=costosOperativos,
                    Kilometraje=form.cleaned_data["Kilometraje"],
                    Tipo=form.cleaned_data["Tipo"],
                    Producto=form.cleaned_data["Producto"],
                    TotalCostos=form.cleaned_data["TotalCostos"],
                    Mop=form.cleaned_data["Mop"],
                    MopPor=form.cleaned_data["MopPor"],
                    TotalTransportista=form.cleaned_data["TotalTransportista"]
                )

                costeo.save()
                return HttpResponseRedirect('/costeo')
            else:
                messages.error(request, "Error")
        context = {
            "form": form,
            "costeo": costeo,
            'depreciacion': depreciacion,
            'FactoresPremisas': factoresPremisas,

        }
        return render(request, "Costeo.html", context)
    else:
        return HttpResponse('test false')

def updateCosteo(request, id):
    if request.user.is_authenticated:
        costeo=get_object_or_404(Costeo, pk=id)
        depreciacion = get_object_or_404(Depreciacion, pk=costeo.IDDepreciacion.id)
        factoresPremisas = get_object_or_404(FactoresPremisas, pk=costeo.IDFactoresPremisas.id)
        costosOperativos = get_object_or_404(CostosOperativos, pk=costeo.IDCostosOperativos.id)
        update=1
        form = CosteoForm(instance=costeo)
        if request.method == "POST":

            form = CosteoForm(request.POST)
            if form.is_valid():
                
                depreciacion.Meses=request.POST['mesesId']
                depreciacion.CostosUnidad=request.POST['costosUnidadId']
                depreciacion.CostosCaja=request.POST['costosCajaId']
                depreciacion.ViajesMes=request.POST['viajesMesId']
                depreciacion.KmsMesXunidad=request.POST['kmsMesXunidadId']
                depreciacion.KmsMaximo=request.POST['kmsMaximoId']
                depreciacion.DepTracto=request.POST['depTractoId']
                depreciacion.DepCaja=request.POST['depCajaId']
                depreciacion.RentaGPS=request.POST['rentaGPSId']
                depreciacion.PlacasTenencia=request.POST['placasTenenciaId']
                depreciacion.Seguro=request.POST['seguroId']
                depreciacion.Admvo=request.POST['admvoId']
                depreciacion.Financieros=request.POST['financierosId']
                depreciacion.MttoUnidadXkm=request.POST['mttoUnidadXkmId']
                depreciacion.Llantas=request.POST['llantasId']
                depreciacion.Operador=request.POST['operadorId']
                depreciacion.DobleOp=request.POST['dobleOpId']
                depreciacion.save()

                factoresPremisas.Unidad=request.POST['unidadId']
                factoresPremisas.KmSencillo=request.POST['kmSencilloId'],
                factoresPremisas.KmRoundTrip=request.POST['kmRoundTripId']
                factoresPremisas.KmMensuales=request.POST['kmMensualesId']
                factoresPremisas.CasetaSingle=request.POST['casetaSingleId']
                factoresPremisas.Rendimiento=request.POST['rendimientoId']
                factoresPremisas.Diesel=request.POST['dieselId']
                factoresPremisas.DieselSinIva=request.POST['dieselSinIvaId']
                factoresPremisas.save()

                costosOperativos.Combustible=request.POST['CombustibleId']
                costosOperativos.Casetas=request.POST['CasetasId']
                costosOperativos.Operador=request.POST['OperadorId']
                costosOperativos.Subtotal1=request.POST['SubTotalId']
                costosOperativos.MttoUnidad=request.POST['MttoUnidadId']
                costosOperativos.LlantasUnidad=request.POST['LlantasUnidadId']
                costosOperativos.Gps=request.POST['GPSId']
                costosOperativos.Seguro=request.POST['SeguroId']
                costosOperativos.PlacasTenencia=request.POST['PlacasTenenciaCostId']
                costosOperativos.SubTotal2=request.POST['SubTotal2Id']
                costosOperativos.Admvo=request.POST['AdmvoId']
                costosOperativos.Financieros=request.POST['FinancierosId']
                costosOperativos.DeprUnidad=request.POST['DeprUnidadId']
                costosOperativos.DeprRemolque=request.POST['DeprRemolqueId']
                costosOperativos.Subtotal3=request.POST['SubTotal3Id']
                costosOperativos.save()

                costeo.Kilometraje=form.cleaned_data["Kilometraje"]
                costeo.Tipo=form.cleaned_data["Tipo"]
                costeo.Producto=form.cleaned_data["Producto"]
                costeo.TotalCostos=form.cleaned_data["TotalCostos"]
                costeo.Mop=form.cleaned_data["Mop"]
                costeo.MopPor=form.cleaned_data["MopPor"]
                costeo.TotalTransportista=form.cleaned_data["TotalTransportista"]
                costeo.save()

                return HttpResponseRedirect('/costeo')
            else:
                messages.error(request, "Error")
            
        context = {
            "form": form,
            "update":update,
            "costeo": costeo,
            'depreciacion': depreciacion,
            'FactoresPremisas': factoresPremisas,

        }
        return render(request, "Costeo.html", context)
    else:
        return HttpResponse('test false')

def loadCosteo(request, id):
    data = dict()

    costeo = get_object_or_404(Costeo, pk=id)
    data['Costeo_html'] = render_to_string('PartialCosteo.html', {
        'costeo': costeo
    })

    return JsonResponse(data)


def cotizacion(request):
    if request.user.is_authenticated:
        form = CotizacionForm()
        if request.method == "POST":

            form = CotizacionForm(request.POST)
            if form.is_valid():
                cotizacion = Cotizacion(
                    CpOrigen=form.cleaned_data['CpOrigen'],
                    CpDestino=form.cleaned_data['CpDestino'],
                    IDTipoUnidad=form.cleaned_data['IDTipoUnidad'],
                    Productos=form.cleaned_data['IDTipoUnidad'],
                    Peso=form.cleaned_data['IDTipoUnidad']
                )
                return HttpResponseRedirect('/cotizacion')
            else:
                messages.error(request, "Error")
        context = {
            'form': form
        }
        return render(request, "cotizacion.html", context)
    else:
        return HttpResponse('test false')


def cotizacionProcess(request):
    print("first")
    if request.is_ajax():
        request_data = request.POST
        data = json.loads(request_data['data'])

        rutas = carrier_models.rutas_models.Rutas.objects.all().filter(CiudadOrigen=data['ciudadOrigen'],
                                                                       CiudadDestino=data['ciudadDestino'],
                                                                       EstadoOrigen=data['EstadoOrigen'],
                                                                       EstadoDestino=data['EstadoDestino']
                                                                       )
        print("second")
        if rutas:
            print("third")
            if data['RangoPrecio']:
                print("fourth")
                if data['TipoUnidad']:
                    print("fifth")
                    unidad=carrier_models.Unidad.objects.get(pk=data['TipoUnidad'])
                    cotizacion = Costeo.objects.all().filter(IDRuta=rutas[0],TotalTransportista__lte= data['RangoPrecio'],IDUnidad=unidad).order_by('TotalTransportista')
                    if cotizacion.exists() == False:
                        data['Error'] = True
                        data['ErrorType'] = "Error: no se encuentran Cotizacion con esa unidad" 
                else:
                    print("fifth else")
                    cotizacion = Costeo.objects.all().filter(IDRuta=rutas[0],TotalTransportista__lte= data['RangoPrecio']).order_by('TotalTransportista')
                    if cotizacion.exists() == False:
                        data['Error'] = True
                        data['ErrorType'] = "Error: no se encuentran Cotizacion con ese rango" 
            else:
                print("fourth else")
                if data['TipoUnidad']:
                    unidad=carrier_models.Unidad.objects.get(pk=data['TipoUnidad'])
                    cotizacion = Costeo.objects.all().filter(IDRuta=rutas[0],IDUnidad=unidad).order_by('TotalTransportista')
                    if cotizacion.exists() == False:
                        data['Error'] = True
                        data['ErrorType'] = "Error: no se encuentran Cotizacion con esa unidad" 
                else:
                    print("sixth else")
                    cotizacion = Costeo.objects.all().filter(IDRuta=rutas[0]).order_by('TotalTransportista')
            if cotizacion:
                print("seventh")
                data = dict()
                data['Error'] = False
                data['Cotizacionlist_list'] = render_to_string('partialCotizacionlist.html', {
                                                       'cotizacion': cotizacion,
                                                       })
        else:
            print("second else")
            data['Error'] = True
            data['ErrorType'] = "Error: selecciona una ruta o introduce los codigos postales"
        print("final")
        return JsonResponse(data)


"""
def saveCosteo(request,form, template_name,id):
    user = request.user
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            if id == -1:
                equipo = Equipo(
                    Carrier=form.cleaned_data["Carrier"],
                    NoUnidades=form.cleaned_data["NoUnidades"],
                    Destinos=form.cleaned_data["Destinos"],
                    Estatus=form.cleaned_data["Estatus"],
                    UsuarioAlta=request.user,
                    UsuarioMod=request.user,
                )
            else:
                equipo = get_object_or_404(Equipo, pk=id)
                equipo.Carrier=form.cleaned_data["Carrier"]
                equipo.NoUnidades=form.cleaned_data["NoUnidades"]
                equipo.Destinos=form.cleaned_data["Destinos"]
                equipo.Estatus=form.cleaned_data["Estatus"]
                equipo.UsuarioMod=request.user
                equipo.date_Mod=datetime.now()
            equipo.save()
            data['form_is_valid'] = True
            equipo=Equipo.objects.all()
            data['Equipo_list'] = render_to_string('partialEquipo_list.html', {
                'equipo': equipo, 'user':user
            })
        else:
            data['form_is_valid'] = False

    context = {'form': form}

    data['html_form'] = render_to_string(template_name,
        context,
        request=request,
    )
    return JsonResponse(data)

def createCosteo(request):
    if request.method == 'POST':
        form = availabilityForm(request.POST)
    else:
        form = availabilityForm()
    return save(request, form, 'partialEquipo_create.html',-1)

def updateCosteo(request, id):
    equipo = get_object_or_404(Equipo, pk=id)
    if request.method == 'POST':
        form = availabilityForm(request.POST, instance=equipo)
    else:
        form = availabilityForm(instance=equipo)
    return save(request, form, 'partialEquipo_update.html',id)"""
