from django.views.generic import ListView
from buildings.models import House
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

class IndexView(ListView):
    template_name = 'gallery.html'
    model = House

    def get_queryset(self):
        news_list = House.objects.all()
        pagination = Paginator(news_list, 6)
        try:
            result = pagination.page(self.request.GET.get('page'))
        except PageNotAnInteger:
            result = pagination.page(1)
        except EmptyPage:
            result = pagination.page(pagination.num_pages)
        return result