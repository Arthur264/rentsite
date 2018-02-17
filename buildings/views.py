from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import House
# Create your views here.
def index(request):
    houses = House.objects.all()
    args = {}
    args["houses"] = houses
    return render(request, 'home.html', args)

def details(request, slug):
    try:
        house = House.objects.get(slug=slug)
        args = {}
        args["house"] = house
    except:
        raise Http404("House not found.")
    return render(request, 'details.html', args)