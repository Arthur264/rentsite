from django.views.generic import DeleteView, ListView
from buildings.models import House
# Create your views here.


class IndexView(ListView):
    template_name = 'properties.html'
    model = House

    def get_queryset(self):
        return House.objects.all()