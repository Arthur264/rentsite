from django.views.generic import ListView
from buildings.models import House
# Create your views here.

class IndexView(ListView):
    template_name = 'gallery.html'
    model = House