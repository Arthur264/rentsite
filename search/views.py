from django.views.generic import ListView
from buildings.models import House


class IndexView(ListView):
    template_name = 'search.html'

    def get_queryset(self):
        print (self.request.GET)
        return House.objects.all()
