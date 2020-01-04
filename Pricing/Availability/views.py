from django.shortcuts import render, redirect,get_object_or_404
from django.core import serializers
from Availability.forms import availabilityForm, availabilityUpdateForm,availabilityDisponibilidadform
from Availability.models import EquipoDisponible
from Transportista import models as carrier_models
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django import forms
from django.template.loader import render_to_string
from datetime import datetime
from django.db.models import Count
# Create your views here.
def disponibilidad(request):
    if (request.user.is_authenticated):
        equipo=EquipoDisponible.objects.all().select_related('rutas').select_related('Carrier')
        total=0
        test=EquipoDisponible.objects.all().count()
        print(test)
        for e in equipo:
            total+=e.Disponibles

       
        context = {
            "equipo":equipo,
            "total":total,
        }
        return render(request, "disponibilidad.html", context)
    else:
        return HttpResponseRedirect('/')

def save(request,form, template_name,id):
    user = request.user
    data = dict()
    total=0
    if request.method == "POST":
        if form.is_valid():
            if id == -1:
                equipo = EquipoDisponible(
                    Carrier=get_object_or_404(carrier_models.Transportista, pk=form.cleaned_data["Carrier"]),
                    rutas=get_object_or_404(carrier_models.rutas_models.Rutas, pk=form.cleaned_data["Rutas"]),
                    Disponibles=form.cleaned_data["NoUnidades"],
                    Ocupado=0,
                    NoUnidades=form.cleaned_data["NoUnidades"]
                )
            else:
                equipo = get_object_or_404(EquipoDisponible, pk=id)
                if form.cleaned_data["NoUnidades"]-equipo.Ocupado > 0 :
                    equipo.NoUnidades=form.cleaned_data["NoUnidades"]
                    equipo.Disponibles=equipo.NoUnidades-equipo.Ocupado
                    equipo.save()
            data['form_is_valid'] = True
            equipo=EquipoDisponible.objects.all()
            for e in equipo:
                total+=e.Disponibles
            data['equipoTotal'] = total
            data['Equipo_list'] = render_to_string('partialEquipo_list.html', {
                'equipo': equipo, 'user':user
            })
        else:
            data['form_is_valid'] = False

    if id != -1:
        transport = get_object_or_404(EquipoDisponible, pk=id)
        context = {'transport': transport,'form': form}
    else:
        context = {'form': form}
    data['html_form'] = render_to_string(template_name,
        context,
        request=request,
    )
    return JsonResponse(data)

def create(request):
    if request.method == 'POST':
        form = availabilityForm(request.POST)
    else:
        form = availabilityForm()
    return save(request, form, 'partialEquipo_create.html',-1)

def update(request, id):
    equipo = get_object_or_404(EquipoDisponible, pk=id)
    if request.method == 'POST':
        form = availabilityUpdateForm(request.POST, instance=equipo)
        templename='partialEquipo_update2.html'
    else:
        form = availabilityUpdateForm(instance=equipo)
        templename='partialEquipo_update2.html'
    return save(request, form,templename ,id)

def delete(request, id):
    user = request.user
    equipo = get_object_or_404(EquipoDisponible, pk=id)
    data = dict()
    if request.method == 'POST':
        equipo.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        equipo = EquipoDisponible.objects.all()
        data['Equipo_list'] = render_to_string('partialEquipo_list.html', {
            'equipo': equipo, 'user':user
        })
    else:
        context = {'equipo': equipo}
        data['html_form'] = render_to_string('partialEquipo_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def updateCarrier(request, id):
    total=0
    user = request.user
    equipo = get_object_or_404(EquipoDisponible, pk=id)
    data = dict()
    if request.method == 'POST':
        form = availabilityDisponibilidadform(request.POST, instance=equipo)
    else:
        form = availabilityDisponibilidadform(instance=equipo)
    template_name = 'partialEquipo_updateCarrier.html'

    if request.method == "POST":
        if form.is_valid():
            data['form_is_valid'] = True
            equipo.Disponibles=form.cleaned_data["Disponibles"]
            equipo.Ocupado=form.cleaned_data["Ocupado"]
            equipo.save()
            equipo = EquipoDisponible.objects.all()
            data['Equipo_list'] = render_to_string('partialEquipo_list.html', {
                'equipo': equipo, 'user':user
            })
            for e in equipo:
                total+=e.Disponibles
            data['equipoTotal'] = total
        else:
            data['form_is_valid'] = False

    context = {'form': form,'equipo':equipo}

    data['html_form'] = render_to_string(template_name,
        context,
        request=request,
    )
    return JsonResponse(data)