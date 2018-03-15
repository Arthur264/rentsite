from django.views.generic import ListView
from buildings.models import House
from buildings.filter import HouseFilter
from django.core import serializers
class IndexView(ListView):
    template_name = 'search.html'

    def get_queryset(self):
        content = {}
        content['filter'] = HouseFilter(self.request.GET, queryset=House.objects.all()).qs
        content['filtermap'] = []
        for item in content['filter']:
            obj = {}
            obj['title'] = str(item.title)
            obj['price'] = str(item.price)
            obj['lat'] = item.houselocation.location.y
            obj['lng'] = item.houselocation.location.x
            obj['thumb'] = item.image_url.url
            obj['url'] = ''
            obj['icon'] = "http:\/\/realhomes-modern.inspirythemes.biz\/wp-content\/themes\/realhomes\/assets\/modern\/images\/map\/single-family-home-map-icon.png"
            obj["retinaIcon"] = "http:\/\/realhomes-modern.inspirythemes.biz\/wp-content\/themes\/realhomes\/assets\/modern\/images\/map\/single-family-home-map-icon@2x.png"
            content['filtermap'].append(obj)
        return content
