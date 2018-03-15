from django.views.generic import ListView
from buildings.models import House
from buildings.filter import HouseFilter
from django.core import serializers
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class IndexView(ListView):
    template_name = 'search.html'
    
    def get_queryset(self):
        content = {}
        datafilter = HouseFilter(self.request.GET, queryset=House.objects.all()).qs
        pagination = Paginator(datafilter, 6)
        try:
            content['filter'] = pagination.page(self.request.GET.get('page'))
        except PageNotAnInteger:
            content['filter'] = pagination.page(1)
        except EmptyPage:
            content['filter'] = pagination.page(pagination.num_pages)
            
        content['filtermap'] = []
        for item in content['filter']:
            obj = {}
            obj['title'] = str(item.title)
            obj['price'] = str(item.price)
            obj['lat'] = str(item.houselocation.location.y)
            obj['lng'] = str(item.houselocation.location.x)
            obj['thumb'] = str(item.image_url.url)
            obj['url'] = str(reverse('house:details' , kwargs={'slug': item.slug}))
            obj['icon'] = ""
            obj["retinaIcon"] = ""
            content['filtermap'].append(obj)
        return content
