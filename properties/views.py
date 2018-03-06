from django.views.generic import DeleteView, ListView, View
from buildings.models import House
from django.shortcuts import render
# Create your views here.


class IndexView(ListView):
    template_name = 'properties.html'
    model = House

    def get_queryset(self):
        return House.objects.all()


class Card(View):
    def get(self, request):
        template_name = "houseTemplate.html"
        card = House.objects.all()

        print(request.GET["search"])
        return render(request, "houseTemplate.html", {'card': card})

