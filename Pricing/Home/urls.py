from django.urls import path, include

from .views import Home, redireccionar, sendmail, testredirect,TESTMETRONIC,TestJson

app_name = 'Home'

urlpatterns = [
    path('', redireccionar, name='redireccionar'),
    path('Home/', Home, name='Home'),
    path('sendmail/<int:test>/', sendmail, name='sendmail'),
    path('testredirect', testredirect, name='testredirect'),
    path('TESTMETRONIC', TESTMETRONIC, name='TESTMETRONIC'),
    path('TestJson', TestJson, name='TestJson')

]