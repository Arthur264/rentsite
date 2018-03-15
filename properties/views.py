from django.views.generic import DeleteView, ListView, View, TemplateView
from buildings.models import House
from django.shortcuts import render
from django.http import JsonResponse
from buildings.models import HouseFavorites
from buildings.templatetags.filter import price
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
# Create your views here.


class IndexView(TemplateView):
    template_name = 'properties.html'


class Card(View):
    def get(self, request):
        if int(request.GET['json']) == 0:
            userfavorites = HouseFavorites.objects.filter(user_id=int(request.user.id)).values_list('house_id',
                                                                                                   flat=True)
            try:
                sortby = request.GET['sortby']
                card = House.objects.order_by(sortby)
            except MultiValueDictKeyError:
                card = House.objects.all()

            pagination = Paginator(card, 6)
            try:
                result = pagination.page(self.request.GET.get('page'))
            except PageNotAnInteger:
                result = pagination.page(1)
            except EmptyPage:
                result = pagination.page(pagination.num_pages)
            return render(request, "cardTemplate.html", {'card': result, 'userfavorites': userfavorites})
        else:
            sortby = request.GET['sortby']
            card = House.objects.order_by(sortby)
            result = []
            for item in card:
                obj = {}
                obj['title'] = item.title
                obj['price'] = '$' + price(item.price)
                obj['lat'] = item.houselocation.location.y
                obj['lng'] =  item.houselocation.location.x
                obj['thumb'] = item.image_url.url
                obj['url'] = reverse('house:details' , kwargs={'slug': item.slug})
                obj["icon"] = "http:\/\/realhomes-modern.inspirythemes.biz\/wp-content\/themes\/realhomes\/assets\/modern\/images\/map\/single-family-home-map-icon.png"
                obj["retinaIcon"] = "http:\/\/realhomes-modern.inspirythemes.biz\/wp-content\/themes\/realhomes\/assets\/modern\/images\/map\/single-family-home-map-icon@2x.png"
                result.append(obj)
            return JsonResponse(result, safe=False)
