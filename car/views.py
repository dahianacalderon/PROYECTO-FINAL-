from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'car.html')

