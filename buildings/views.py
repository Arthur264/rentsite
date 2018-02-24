from django.shortcuts import get_list_or_404
from .models import House, HouseImage
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
        content['imagehouse'] = get_list_or_404(HouseImage, house=content["house"].pk)
        return content
