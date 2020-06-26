from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from TransportistasProspecto.models import Prioridades, Estatus, Tipos
@login_required

def Home(request):
	if (request.user.is_authenticated):
		return render(request,'Home.html')
	else:
		return HttpResponseRedirect('/')

def redireccionar(request):
	if (request.user.is_authenticated):
		return HttpResponseRedirect('Home')
	else:
		return HttpResponseRedirect('/accounts/login')