from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import disponibilidad, create, update, delete, updateCarrier
from Availability import views

app_name = 'Availability'

urlpatterns = [
    path('', disponibilidad, name='disponibilidad'),
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
 	path('delete/<int:id>/', delete, name='delete'),
 	path('updateCarrier/<int:id>/', updateCarrier, name='updateCarrier'),
]
