from django.urls import path, include
from car.views import *

urlpatterns = [
    path('', inicio, name="car")
]
