from django.shortcuts import render, redirect,get_object_or_404
from django.core import serializers
from Rutas.forms import RutasForm, RutasUpForm
from Rutas.models import Rutas
from Transportista import models as Carrier_Model
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django import forms
import django_excel as excel
from django.contrib.auth.decorators import login_required
@login_required
def routes(request):
    if (request.user.is_authenticated):
        routes=Rutas.objects.all()
        form = RutasForm(request.POST)
        if request.method == "POST":
            form = RutasForm(request.POST)
            if form.is_valid():
                routes = Rutas(
                    CPOrigen=form.cleaned_data["CPOrigen"],
                   	CiudadOrigen=form.cleaned_data["CiudadOrigen"],
                    EstadoOrigen=form.cleaned_data["EstadoOrigen"],
                    CPDestino=form.cleaned_data["CPDestino"],
                    CiudadDestino=form.cleaned_data["CiudadDestino"],
                    EstadoDestino=form.cleaned_data["EstadoDestino"],
                    ViajeRedondo=form.cleaned_data["ViajeRedondo"],
                    NombreRuta=form.cleaned_data["NombreRuta"],
                    Kilometros=form.cleaned_data["Kilometros"],
                    Casetas=form.cleaned_data["Casetas"],
                    IDUsuarioAlta=request.user,
                    IDUsuarioMod=request.user,
                )
                routes.save()
                return HttpResponseRedirect('/routes')
            else:
                messages.error(request, "Error")
        context = {
            "form": form,
            "routes":routes,

        }
        return render(request, "routes.html", context)
    else:
        return HttpResponseRedirect('/')

def loadCarriers(request):
    Carrier = Carrier_Model.Transportista.objects.all()
    serialized_queryset = serializers.serialize('python', Carrier)
    return JsonResponse(serialized_queryset, safe=False)

def routesUpdate(request, id):
     if request.user.is_authenticated:  
        rutas = get_object_or_404(Rutas, pk=id)
        form = RutasUpForm(instance=rutas)
        carriers = Carrier_Model.Transportista.objects.all().filter(IDRutas=rutas)

        if request.method == "POST":
            form = RutasUpForm(request.POST, instance=rutas)  
            if form.is_valid():
                rutas.CPOrigen = form.cleaned_data["CPOrigen"]
                rutas.CiudadOrigen = form.cleaned_data["CiudadOrigen"]
                rutas.EstadoOrigen = form.cleaned_data["EstadoOrigen"]
                rutas.CPDestino = form.cleaned_data["CPDestino"]
                rutas.CiudadDestino = form.cleaned_data["CiudadDestino"]
                rutas.EstadoDestino = form.cleaned_data["EstadoDestino"]
                rutas.ViajeRedondo = form.cleaned_data["ViajeRedondo"]
                rutas.NombreRuta = form.cleaned_data["NombreRuta"]
                rutas.Kilometros = form.cleaned_data["Kilometros"]
                rutas.save()
                return redirect('Rutas:routes')
            
        context = {
            'carriers':carriers,
            'form': form,
            'rutas':rutas,
            

        }
        return render(request, 'routesUpdate.html', context) 