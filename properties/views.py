from django.views.generic import DeleteView, ListView, View
from buildings.models import House
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


class IndexView(ListView):
    template_name = 'properties.html'
    model = House

    def get_queryset(self):
        return House.objects.all()


class Card(View):
    def get(self, request):
        try:
            sortby = request.GET['sortby']
            card = House.objects.order_by(sortby)
        except MultiValueDictKeyError:
            card = House.objects.all()
        return render(request, "houseTemplate.html", {'card': card})

