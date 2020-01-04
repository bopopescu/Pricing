from django.shortcuts import render, redirect,get_object_or_404
from django.core import serializers
from Transportista.forms import (TransportistaForm,UpTransportistaForm, ExtrasForm, ExpedienteFAltaForm,ExpedienteActaConsti,
ExpedienteCedFis,ExpedienteIFE,ExpedienteComDom,ExpedienteCarBan,ExpedienteConCon,ExpedienteConSer,ExpedienteConTar,
ExpedienteDes,ExpedientePer,ExpedienteLic,TarjetaDirForm,TarjetaVentForm,BitacoraForm,UnidadesForm,registroTarjetaForm,
placasTraserasForm,seguroForm,UnidadTypeForm,TarifasForm,RemolqueForm,AddRutasForm)
from Transportista.models import Transportista, Extras,Expediente,Bitacora,Unidad,UnidadType,Tarifas,Remolque
from users import models as Users_models
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse,HttpResponseNotFound
from django import forms
import django_excel as excel
from django_tables2 import RequestConfig
from django.forms.models import model_to_dict
from django.http import JsonResponse
from datetime import datetime
from django.template.loader import render_to_string
from Rutas import models as rutas_models
from django.contrib.auth.decorators import login_required
@login_required
def carrier(request):
    if (request.user.is_authenticated):
        carriers=Transportista.objects.all()
        form = TransportistaForm(request.POST)
        if request.method == "POST":
            form = TransportistaForm(request.POST)
            if form.is_valid():
                transportista = Transportista(
                    RazonSocial=form.cleaned_data["RazonSocial"],
                   	Email=form.cleaned_data["Email"],
                    NombreComercial=form.cleaned_data["NombreComercial"],
                    Calle=form.cleaned_data["Calle"],
                    Estado=form.cleaned_data["Estado"],
                    Ciudad=form.cleaned_data["Ciudad"],
                    NumInt=form.cleaned_data["NumInt"],
                    NumExt=form.cleaned_data["NumExt"],
                    CP=form.cleaned_data["CP"],
                    Colonia=form.cleaned_data["Colonia"],
                    BaseTerminal=form.cleaned_data["BaseTerminal"],
                    Telefonos=form.cleaned_data["Telefonos"],
                    PaginaWeb=form.cleaned_data["PaginaWeb"],
                    Credito=form.cleaned_data["Credito"],
                    NombreContacto=form.cleaned_data["NombreContacto"],
                    IDUsuarioAlta=request.user.id,
                    IDUsuarioMod=request.user.id,
                )
                transportista.save()
                return HttpResponseRedirect('/carrier')
            else:
                messages.error(request, "Error")
        context = {
            "form": form,
            "carriers":carriers,

        }
        return render(request, "carrier.html", context)
    else:
        return HttpResponseRedirect('/')

def carrierup(request):
    if (request.user.is_authenticated):
        form = TransportistaForm(request.POST)
        if request.method == "POST":
            form = TransportistaForm(request.POST)
            if form.is_valid():
                transportista = Transportista(
                    RazonSocial=form.cleaned_data["RazonSocial"],
                    Email=form.cleaned_data["Email"],
                    NombreComercial=form.cleaned_data["NombreComercial"],
                    Dirreccion=form.cleaned_data["Dirreccion"],
                    Estado=form.cleaned_data["Estado"],
                    Ciudad=form.cleaned_data["Ciudad"],
                    CP=form.cleaned_data["CP"],
                    Colonia=form.cleaned_data["Colonia"],
                    BaseTerminal=form.cleaned_data["BaseTerminal"],
                    Telefonos=form.cleaned_data["Telefonos"],
                    PaginaWeb=form.cleaned_data["PaginaWeb"],
                    Credito=form.cleaned_data["Credito"],

                )
                transportista.save()
                return HttpResponseRedirect('/carrier')
            else:
                messages.error(request, "Error")
        context = {
            "form": form,

        }
        return render(request, "carrier.html", context)
    else:
        return HttpResponseRedirect('/')

class UploadFileForm(forms.Form):
    file = forms.FileField()

def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        def choice_func(row):
            q = Transportista().objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Transportista],
                initializers=[None, choice_func],
                mapdicts=[
                    ['RazonSocial', 'Email', 'NombreComercial', 'Calle', 'Estado', 'Ciudad', 'CP', 'Colonia', 'BaseTerminal', 'Telefonos', 'PaginaWeb', 'Credito', 'Date_joined', 'Is_active', 'NumExt', 'NUmInt', 'NombreContacto']]
            )
            return redirect('Transportista:carrier')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })
@login_required
def carrierview(request, id, bandModal):
    if (request.user.is_authenticated):
        if(Extras.objects.filter(IDTransportista_id=id).exists()):
            Extra=Extras.objects.get(IDTransportista_id=id)
        else:
            Extra=[]
        if(Expediente.objects.filter(IDTransportista_id=id).exists()):
            ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
        else:
            ExpedienteTemp=[]
        if(Bitacora.objects.filter(IDTransportista_id=id).exists()):
            bitacora=Bitacora.objects.all().filter(IDTransportista_id=id)
        else:
            bitacora=[]
        transport=Transportista.objects.get(pk=id)
        form = ExtrasForm()
        formExpAlta=ExpedienteFAltaForm()
        formActaConsti=ExpedienteActaConsti()
        formCedFis=ExpedienteCedFis()
        formIFE=ExpedienteIFE()
        formComDom=ExpedienteComDom()
        formCarBan=ExpedienteCarBan()
        formConCon=ExpedienteConCon()
        formConSer=ExpedienteConSer()
        formConTar=ExpedienteConTar()
        formDes=ExpedienteDes()
        formPer=ExpedientePer()
        formLic=ExpedienteLic()
        formTarDir=TarjetaDirForm()
        formTarVent=TarjetaVentForm()
        formBitac=BitacoraForm()
        if request.method == "POST":
            form = ExtrasForm(request.POST, request.FILES)
            formExpAlta=ExpedienteFAltaForm(request.POST, request.FILES)
            formActaConsti=ExpedienteActaConsti(request.POST, request.FILES)
            formCedFis=ExpedienteCedFis(request.POST, request.FILES)
            formIFE=ExpedienteIFE(request.POST, request.FILES)
            formComDom=ExpedienteComDom(request.POST, request.FILES)
            formCarBan=ExpedienteCarBan(request.POST, request.FILES)
            formConCon=ExpedienteConCon(request.POST, request.FILES)
            formConSer=ExpedienteConSer(request.POST, request.FILES)
            formConTar=ExpedienteConTar(request.POST, request.FILES)
            formDes=ExpedienteDes(request.POST, request.FILES)
            formPer=ExpedientePer(request.POST, request.FILES)
            formLic=ExpedienteLic(request.POST, request.FILES)
            formTarDir=TarjetaDirForm(request.POST, request.FILES)
            formTarVent=TarjetaVentForm(request.POST, request.FILES)
            formBitac=BitacoraForm(request.POST, request.FILES)
            if form.is_valid():
                if(Extras.objects.filter(IDTransportista_id=id).exists()):
                    Extra=Extras.objects.get(IDTransportista_id=id)
                    Extra.Image=form.cleaned_data["Image"]
                    Extra.save()
                else:
                    Extra = Extras(
                        IDTransportista=transport,
                        Image=form.cleaned_data["Image"],
                    )
                    Extra.save()
                return redirect('Transportista:carrierview',id=id,bandModal=0)
            else:
                messages.error(request, "Error")
            if formExpAlta.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.FormatoAlta=formExpAlta.cleaned_data["FormatoAlta"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        FormatoAlta=formExpAlta.cleaned_data["FormatoAlta"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formActaConsti.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.ActaConstitutiva=formActaConsti.cleaned_data["ActaConstitutiva"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        ActaConstitutiva=formActaConsti.cleaned_data["ActaConstitutiva"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formCedFis.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.CedulaFiscal=formCedFis.cleaned_data["CedulaFiscal"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        cedulaFiscal=formCedFis.cleaned_data["CedulaFiscal"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formIFE.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.IFERepresentante=formIFE.cleaned_data["IFERepresentante"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        iFERepresentante=formIFE.cleaned_data["IFERepresentante"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formComDom.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.ComprobanteDomicilio=formComDom.cleaned_data["ComprobanteDomicilio"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        comprobanteDomicilio=formComDom.cleaned_data["ComprobanteDomicilio"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formCarBan.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.CaratulaBancaria=formCarBan.cleaned_data["CaratulaBancaria"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        caratulaBancaria=formCarBan.cleaned_data["CaratulaBancaria"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formConCon.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.ConvenioConfidencialidad=formConCon.cleaned_data["ConvenioConfidencialidad"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        ConvenioConfidencialidad=formConCon.cleaned_data["ConvenioConfidencialidad"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formConSer.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.ContratoServicios=formConSer.cleaned_data["ContratoServicios"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        contratoServicios=formConSer.cleaned_data["ContratoServicios"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formConTar.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.ConvenioTarifas=formConTar.cleaned_data["ConvenioTarifas"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        ConvenioTarifas=formConTar.cleaned_data["ConvenioTarifas"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formDes.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.Descripcion=formDes.cleaned_data["Descripcion"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        descripcion=formDes.cleaned_data["Descripcion"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")

            if formPer.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.Permisos=formPer.cleaned_data["Permisos"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        permisos=formPer.cleaned_data["Permisos"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formLic.is_valid():
                if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                    ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                    ExpedienteTemp.Licencias=formLic.cleaned_data["Licencias"]
                    ExpedienteTemp.save()
                else:
                    ExpedienteTemp = Expediente(
                        IDTransportista=transport,
                        Licencias=formLic.cleaned_data["Licencias"],
                    )
                    ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
            else:
                messages.error(request, "Error")
            if formTarDir.is_valid():
                if(Extras.objects.filter(IDTransportista_id=id).exists()):
                    Extra=Extras.objects.get(IDTransportista_id=id)
                    Extra.TarjetaDirector=formTarDir.cleaned_data["TarjetaDirector"]
                    Extra.save()
                else:
                    Extra = Extras(
                        IDTransportista=transport,
                        TarjetaDirector=formTarDir.cleaned_data["TarjetaDirector"],
                    )
                    Extra.save()
                return redirect('Transportista:carrierview',id=id,bandModal=0)
            else:
                messages.error(request, "Error")
            if formTarVent.is_valid():
                if(Extras.objects.filter(IDTransportista_id=id).exists()):
                    Extra=Extras.objects.get(IDTransportista_id=id)
                    Extra.TarjetaVentas=formTarVent.cleaned_data["TarjetaVentas"]
                    Extra.save()
                else:
                    Extra = Extras(
                        IDTransportista=transport,
                        TarjetaVentas=formTarVent.cleaned_data["TarjetaVentas"],
                    )
                    Extra.save()
                return redirect('Transportista:carrierview',id=id,bandModal=0)
            else:
                messages.error(request, "Error")
            if formBitac.is_valid():
                bitacora = Bitacora(
                    IDTransportista=transport,
                    Fecha=formBitac.cleaned_data["Fecha"],
                    RepLGK=formBitac.cleaned_data["RepLGK"],
                    RepTransportista=formBitac.cleaned_data["RepTransportista"],
                )
                bitacora.save()
                return redirect('Transportista:carrierview',id=id,bandModal=0)
            else:
                messages.error(request, "Error")

        context = {
            "Expediente" : ExpedienteTemp,
            "Extra" : Extra,
            "transport": transport,
            "form":form,
            "formExpAlta":formExpAlta,
            "bandModal": bandModal,
            "formActaConsti":formActaConsti,
            "formCedFis":formCedFis,
            "formIFE":formIFE,
            "formComDom":formComDom,
            "formCarBan":formCarBan,
            "formConCon":formConCon,
            "formConSer":formConSer,
            "formConTar":formConTar,
            "formDes":formDes,
            "formPer":formPer,
            "formLic":formLic,
            "formTarDir":formTarDir,
            "formTarVent":formTarVent,
            "formBitac":formBitac,
            "Bitacora":bitacora,

        }
        return render(request, "carrierview.html", context)
    else:
        return HttpResponseRedirect('/')
@login_required
def expedienteDelete(request, id,campo):
    print("verifica")
    if (request.user.is_authenticated):
        if(campo == "formatoAlta"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.FormatoAlta.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "actaConstitutiva"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.ActaConstitutiva.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "cedulaFiscal"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.CedulaFiscal.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "iFERepresentante"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.IFERepresentante.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "comprobanteDomicilio"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.ComprobanteDomicilio.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "caratulaBancaria"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.CaratulaBancaria.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "convenioConfidencialidad"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.ConvenioConfidencialidad.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "contratoServicios"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.ContratoServicios.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "convenioTarifas"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.ConvenioTarifas.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "descripcion"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.Descripcion.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "permisos"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.Permisos.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "licencias"):
            if(Expediente.objects.filter(IDTransportista_id=id).exists()):
                ExpedienteTemp=Expediente.objects.get(IDTransportista_id=id)
                ExpedienteTemp.Licencias.delete()
                ExpedienteTemp.save()
                return redirect('Transportista:carrierview',id=id,bandModal=1)
        if(campo == "TarjetaDir"):
            print("test1")
            if(Extras.objects.filter(IDTransportista_id=id).exists()):
                Extra=Extras.objects.get(IDTransportista_id=id)
                Extra.TarjetaDirector.delete()
                Extra.save()
                return redirect('Transportista:carrierview',id=id,bandModal=0)
        if(campo == "TarjetaVen"):
            if(Extras.objects.filter(IDTransportista_id=id).exists()):
                Extra=Extras.objects.get(IDTransportista_id=id)
                Extra.TarjetaVentas.delete()
                Extra.save()
                return redirect('Transportista:carrierview',id=id,bandModal=0)
        if(campo == "imagen"):
            if(Extras.objects.filter(IDTransportista_id=id).exists()):
                Extra=Extras.objects.get(IDTransportista_id=id)
                Extra.Image.delete()
                Extra.save()
                return redirect('Transportista:carrierview',id=id,bandModal=0)
        return redirect('Transportista:carrierview',id=id,bandModal=0)
    else:
        return HttpResponseRedirect('/')

def bitacoraDelete(request,id,idtransportista):
    bitacora = Bitacora.objects.get(id=id)
    bitacora.Active=0
    bitacora.save()
    return redirect('Transportista:carrierview',id=idtransportista,bandModal=0)
    
def carrierDelete(request,id):
    transport=Transportista.objects.get(pk=id)
    transport.Active=0
    transport.save()
    return redirect('Transportista:carrier')
@login_required
def carrierUpdate(request, id):
    if request.user.is_authenticated:  
        transport = get_object_or_404(Transportista, pk=id)  
        form = UpTransportistaForm(request.POST or None, instance=transport)  
        if form.is_valid():
            users=get_object_or_404(Users_models.User, pk=id) 
            transportista = get_object_or_404(Transportista, pk=id) 
            transportista.RazonSocial=form.cleaned_data["RazonSocial"]
            transportista.Email=form.cleaned_data["Email"]
            transportista.NombreComercial=form.cleaned_data["NombreComercial"]
            transportista.Calle=form.cleaned_data["Calle"]
            transportista.Estado=form.cleaned_data["Estado"]
            transportista.Ciudad=form.cleaned_data["Ciudad"]
            transportista.NumInt=form.cleaned_data["NumInt"]
            transportista.NumExt=form.cleaned_data["NumExt"]
            transportista.CP=form.cleaned_data["CP"]
            transportista.Colonia=form.cleaned_data["Colonia"]
            transportista.BaseTerminal=form.cleaned_data["BaseTerminal"]
            transportista.Telefonos=form.cleaned_data["Telefonos"]
            transportista.PaginaWeb=form.cleaned_data["PaginaWeb"]
            transportista.Credito=form.cleaned_data["Credito"]
            transportista.NombreContacto=form.cleaned_data["NombreContacto"]
            transportista.Date_Mod=datetime.now()
            transportista.IDUsuarioMod=users.id
            transportista.save()
            return redirect('Transportista:carrier')
        return render(request, 'carrierUpdate.html', {'form': form}) 
@login_required
def Unidades(request):
    error="FALSE"
    if (request.user.is_authenticated):
        unit=Unidad.objects.all()
        form = UnidadesForm()
        if request.method == "POST":

            form = UnidadesForm(request.POST,request.FILES)
            if form.is_valid():

                unit = Unidad(
                    IDTransportista = get_object_or_404(Transportista, pk=form.cleaned_data["IDTransportista"]),
                    IDTipoUnidad = get_object_or_404(UnidadType, pk=form.cleaned_data["IDUnitType"]),
                    Nombre = form.cleaned_data["Nombre"],
                    Combustible = form.cleaned_data["Combustible"],
                    Performance = form.cleaned_data["Performance"],
                    RegistroVehiculo = form.cleaned_data["RegistroVehiculo"],
                    RegistroTarjeta = form.cleaned_data["RegistroTarjeta"],
                    FechaExpiracion = form.cleaned_data["FechaExpiracion"],
                    Marca = form.cleaned_data["Marca"],
                    Modelo = form.cleaned_data["Modelo"],
                    Anno = form.cleaned_data["Anno"],
                    Placas = form.cleaned_data["Placas"],
                    Econnum = form.cleaned_data["Econnum"],
                    NumeroSatelital = form.cleaned_data["NumeroSatelital"],
                    Special = form.cleaned_data["Special"],
                    FullUnit = form.cleaned_data["FullUnit"],
                    PlacasTraseras = form.cleaned_data["PlacasTraseras"],
                    Seguro = form.cleaned_data["Seguro"],
                )
                unit.save()
                return redirect('Transportista:Unidades')
            else:
                messages.error(request, "Error")
                if(form.errors):
                    if(form.errors['Placas'][0]=="Unidad with this Placas already exists."):
                        error="Ya existe un Tracto con esas placas "

        context = {
            "form": form,
            "unit":unit,
            'error':error,

        }
        return render(request, "unidad.html", context)
    else:
        return HttpResponseRedirect('/') 

def unitUpdate(request, id):
    if request.user.is_authenticated:  
        unit = get_object_or_404(Unidad, pk=id)  
        form = UnidadesForm(request.POST or None, instance=unit)  
        if form.is_valid():
            unit.Nombre = form.cleaned_data["Nombre"]
            unit.Combustible = form.cleaned_data["Combustible"]
            unit.Performance = form.cleaned_data["Performance"]
            unit.Volumen = form.cleaned_data["Volumen"]
            unit.Peso = form.cleaned_data["Peso"]
            unit.Longitud = form.cleaned_data["Longitud"]
            unit.Ancho = form.cleaned_data["Ancho"]
            unit.Special = form.cleaned_data["Special"]
            unit.FullUnit = form.cleaned_data["FullUnit"]
            unit.save()
            return redirect('Transportista:Unidades')
        return render(request, 'UnitUpdate.html', {'form': form}) 

def unitDelete(request,id):
    unit=Unidad.objects.get(pk=id)
    unit.Active=0
    unit.save()
    return redirect('Transportista:Unidades')

def loadUnitTypes(request):
    unit = UnidadType.objects.all()
    serialized_queryset = serializers.serialize('python', unit)
    return JsonResponse(serialized_queryset, safe=False)

def unidadType(request):
    if (request.user.is_authenticated):
        unit=UnidadType.objects.all()
        form = UnidadTypeForm()
        if request.method == "POST":

            form = UnidadTypeForm(request.POST)
            if form.is_valid():

                unit = UnidadType(
                    Nombre = form.cleaned_data["Nombre"],
                    Capacidad = form.cleaned_data["Capacidad"],
                    Medidas = form.cleaned_data["Medidas"],
                    Configuraciones = form.cleaned_data["Configuraciones"],
                    Image = form.cleaned_data["Image"],
                )
                unit.save()
                return redirect('Transportista:unidadType')
            else:
                messages.error(request, "Error")

        context = {
            "form": form,
            "unit":unit,

        }
        return render(request, "UnidadType.html", context)
    else:
        return HttpResponseRedirect('/')
@login_required
def tarifas(request):
    if (request.user.is_authenticated):
        Tarifa=Tarifas.objects.all()
        form = TarifasForm()
        if request.method == "POST":

            form = TarifasForm(request.POST)
            if form.is_valid():

                Tarifa = Tarifas(
                    Equipo = form.cleaned_data["Equipo"],
                    Origen = form.cleaned_data["Origen"],
                    Destino = form.cleaned_data["Destino"],
                    Moneda = form.cleaned_data["Moneda"],
                    Tarifa = form.cleaned_data["Tarifa"],
                    Comentarios = form.cleaned_data["Comentarios"],
                    Evidencia = form.cleaned_data["Evidencia"],
                )
                Tarifa.save()
                return redirect('Transportista:unidadType')
            else:
                messages.error(request, "Error")

        context = {
            "form": form,
            "Tarifa":Tarifa,

        }
        return render(request, "Tarifas.html", context)
    else:
        return HttpResponseRedirect('/')
@login_required
def remolques(request):
    error="FALSE"
    if (request.user.is_authenticated):
        remolque=Remolque.objects.all().select_related('IDTipoUnidad')
        form = RemolqueForm()
        if request.method == "POST":

            form = RemolqueForm(request.POST,request.FILES)
            if form.is_valid():

                remolque = Remolque(
                    IDTransportista = get_object_or_404(Transportista, pk=form.cleaned_data["IDTransportista"]),
                    IDTipoUnidad = get_object_or_404(UnidadType, pk=form.cleaned_data["IDUnitType"]),
                    Nombre = form.cleaned_data["Nombre"],
                    Marca = form.cleaned_data["Marca"],
                    Modelo = form.cleaned_data["Modelo"],
                    Anno = form.cleaned_data["Anno"],
                    Placas = form.cleaned_data["Placas"],
                    Econnum = form.cleaned_data["Econnum"],
                    NumeroSatelital = form.cleaned_data["NumeroSatelital"],
                    Volumen = form.cleaned_data["Volumen"],
                    Peso = form.cleaned_data["Peso"],
                    Longitud = form.cleaned_data["Longitud"],
                    Ancho = form.cleaned_data["Ancho"],
                    PlacasTraseras = form.cleaned_data["PlacasTraseras"],
                    Seguro = form.cleaned_data["Seguro"],
                    FacturaRemolque = form.cleaned_data["FacturaRemolque"],
                    
                )
                remolque.save()
                return redirect('Transportista:remolques')
            else:
                messages.error(request, "Error")
                if(form.errors):
                    if(form.errors['Placas'][0]=="Remolque with this Placas already exists."):
                        error="Ya existe un Tracto con esas placas "

        context = {
            "form": form,
            "remolque":remolque,
            'error':error,

        }
        return render(request, "remolques.html", context)
    else:
        return HttpResponseRedirect('/')

def remolqueDelete(reques, id):
    remolque=Remolque.objects.get(pk=id)
    remolque.Active=0
    remolque.save()
    return redirect('Transportista:remolques')

def getRutaAll(request):
    rutas = rutas_models.Rutas.objects.all()
    serialized_queryset = serializers.serialize('python', rutas)
    return JsonResponse(serialized_queryset, safe=False)
def AddRutas(request, id):
    data = dict()
    form = AddRutasForm()

    if request.method == "POST":
        form = AddRutasForm(request.POST)
        if form.is_valid():
            transportista = get_object_or_404(Transportista, pk=id)
            transportista.IDRutas.add(get_object_or_404(rutas_models.Rutas, pk=form.cleaned_data["IDRutas"]))
            transportista.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
        return redirect('Transportista:carrier')

    context = {
        'carrierid':id,
        'form': form}

    data['html_form'] = render_to_string('partialRutasCarrier.html',
                                         context,
                                         request=request,
                                         )
    return JsonResponse(data)
def unitTypeDelete(request,id):
    unit=UnidadType.objects.get(pk=id)
    unit.Active=0
    unit.save()
    return redirect('Transportista:unidadType')
@login_required
def UpdateUnitType(request, id):
    user = request.user
    unit = get_object_or_404(UnidadType, pk=id)
    data = dict()
    if request.method == 'POST':
        form = UnidadTypeForm(request.POST, instance=unit)
    else:
        form = UnidadTypeForm(instance=unit)
    template_name = 'partial_UnitTypeUpdate.html'

    if request.method == "POST":
        if form.is_valid():
            print("adivino")
            data['form_is_valid'] = True
            unit.Nombre = form.cleaned_data["Nombre"]
            unit.Capacidad = form.cleaned_data["Capacidad"]
            unit.Configuraciones = form.cleaned_data["Configuraciones"]
            unit.save()
            unit = UnidadType .objects.all()
            return redirect('Transportista:unidadType')
        else:
            data['form_is_valid'] = False
            print("second")
            print (form.errors, len(form.errors))

    context = {'form': form,'unit':unit}

    data['html_form'] = render_to_string(template_name,
        context,
        request=request,
    )
    return JsonResponse(data)
