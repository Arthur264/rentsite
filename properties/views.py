from django.views.generic import DeleteView, ListView, View
from buildings.models import House
from django.shortcuts import render
from django.http import JsonResponse
from buildings.templatetags.filter import price 
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


class IndexView(ListView):
    template_name = 'properties.html'
    model = House

    def get_queryset(self):
        return House.objects.all()


class Card(View):
    def get(self, request):
        if int(request.GET['json']) == 0:
            try:
                sortby = request.GET['sortby']
                card = House.objects.order_by(sortby)
            except MultiValueDictKeyError:
                card = House.objects.all()
            return render(request, "cardTemplate.html", {'card': card})
        else:
            sortby = request.GET['sortby']
            card = House.objects.order_by(sortby)
            result = []
            for item in card:
                obj = {}
                obj['title'] = item.title
                obj['price'] = '$' + price(item.price)
                obj['lat'] = "25.637835760899435"
                obj['lng'] = "-80.30060203710934"
                obj['thumb'] = item.image_url.url
                obj['url'] = "http:\/\/realhomes-modern.inspirythemes.biz\/property\/shop-at-southwest-186th-street\/"
                obj["icon"] = "http:\/\/realhomes-modern.inspirythemes.biz\/wp-content\/themes\/realhomes\/assets\/modern\/images\/map\/single-family-home-map-icon.png"
                obj["retinaIcon"] = "http:\/\/realhomes-modern.inspirythemes.biz\/wp-content\/themes\/realhomes\/assets\/modern\/images\/map\/single-family-home-map-icon@2x.png"
                result.append(obj)
                
            return JsonResponse(result,safe=False)
            
            
            
        
