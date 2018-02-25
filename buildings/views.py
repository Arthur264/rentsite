from django.shortcuts import get_list_or_404
from .models import House, HouseImage, HouseDetails
from django.views.generic import CreateView, DeleteView, ListView

# Create your views here.


class IndexView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return House.objects.all()


class DetailsViews(DeleteView):
    template_name = 'details.html'
    model = House

    def get_context_data(self, **kwargs):
        content = super(DetailsViews, self).get_context_data(**kwargs)
        content['imagehouse'] = HouseImage.objects.filter(house=content["house"].pk)
        content['housedetails'] = HouseDetails.objects.filter(house=content["house"].pk)[0]
        return content
