from django.shortcuts import render
from django.http import HttpResponse
from .models import House
# Create your views here.
def index(request):
    houses = House.objects.all();
    args = {}
    args["houses"] = houses
    return render(request, 'home.html', args)