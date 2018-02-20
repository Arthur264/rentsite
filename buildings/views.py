from django.shortcuts import render
from django.http import Http404
from .models import House, HouseImage
# Create your views here.
def index(request):
    houses = House.objects.all()
    args = {}
    args["houses"] = houses
    return render(request, 'home.html', args)

def details(request, slug):
    try:
        house = House.objects.get(slug=slug)
        imagehouse = HouseImage.objects.filter(pk=house.pk)
        print ("test", imagehouse)
        args = {}
        args["house"] = house
        args["imagehouse"] = imagehouse
    except:
        raise Http404("House not found.")
    return render(request, 'details.html', args)