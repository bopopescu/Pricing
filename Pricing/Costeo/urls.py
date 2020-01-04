from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import (Home, costeos, loadTransport, loadRutas, getRuta, loadCosteo, cotizacion, loadUnidades,
                    cotizacionProcess, updateCosteo,firstTime)
from Costeo import views

app_name = 'Costeo'

urlpatterns = [
    path('Home', Home, name='Home'),
    path('loadTransport', loadTransport, name="loadTransport"),
    path('loadUnidades', loadUnidades, name="loadUnidades"),
    path('loadRutas/<int:id>/', loadRutas, name="loadRutas"),
    path('getRuta/<int:id>/', getRuta, name="getRuta"),
    path('', costeos, name='costeos'),
    path('loadCosteo/<int:id>/', loadCosteo, name="loadCosteo"),
    path('cotizacion/', cotizacion, name="cotizacion"),
    path('cotizacionProcess/', cotizacionProcess, name="cotizacionProcess"),
    path('updateCosteo/<int:id>/', updateCosteo, name="updateCosteo"),
    path('firstTime/', firstTime, name="firstTime"),
]
