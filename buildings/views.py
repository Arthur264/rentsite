from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import House, HouseImage
# Create your views here.
def index(request):
    houses = House.objects.all()
    args = {}
    args["houses"] = houses
    return render(request, 'home.html', args)

def details(request, slug):
    house = get_object_or_404(House, slug=slug)
    imagehouse = get_list_or_404(HouseImage, house=house.pk)
    args = {}
    args["house"] = house
    args["imagehouse"] = imagehouse
    return render(request, 'details.html', args)