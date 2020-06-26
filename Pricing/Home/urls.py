from django.urls import path, include

#from .views import Home, redireccionar, sendmail, testredirect,TESTMETRONIC,TestJson
from .views import Home, redireccionar

app_name = 'Home'

urlpatterns = [
    path('', redireccionar, name='redireccionar'),
    path('Home/', Home, name='Home'),
]