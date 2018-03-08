from helpers.objects import get_or_None, filter_or_None
from .models import House, HouseImage, HouseDetails, HouseVisited
from authentication.models import User, UserProfile, Role, UserFavorites
from django.views.generic import CreateView, DeleteView, ListView, View, TemplateView, DetailView
from django.http import HttpResponse, JsonResponse, QueryDict
from django.db import IntegrityError
from django.shortcuts import render
from django.db.models import Count
from django.core import serializers
# Create your views here.
import json

class IndexView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return House.objects.all()

    def get_context_data(self, **kwargs):
        content = super(IndexView, self).get_context_data(**kwargs)
        content['agents'] = filter_or_None(UserProfile, user_role=Role.objects.get(name="Agent").pk)
        # content['agents']['tex'] = "dsfh"
        # for item in  content['agents']:
        #     print (get_or_None(User, pk= str(item.user_id)))
        return content


class DetailsViews(DetailView):
    template_name = 'details.html'
    model = House

    def get_context_data(self, **kwargs):
        content = super(DetailsViews, self).get_context_data(**kwargs)
        DetailsViews.add_count(self, self.request, content)
        content['imagehouse'] = filter_or_None(HouseImage, house=content["house"].pk)
        content['housedetails'] = get_or_None(HouseDetails, house=content["house"].pk)
        return content

    def add_count(self, request, content):
        try:
            visited = HouseVisited(user=request.user, house=content['house'])
            visited.save()
            return True
        except:
            return False


class FavoritesView(View):
    def post(self, request):
        try:
            favorite = UserFavorites(user_id=int(request.user.id), house_id=int(request.POST["house"]))
            favorite.save()
            return JsonResponse({'success': 1})
        except IntegrityError:
            return JsonResponse({'success': 0})

    def get(self, request):
        try:
            favorite = UserFavorites.objects.filter(user_id=int(request.user.id))
            return render(request, "cardTemplate.html", {'favorites': favorite})
        except Exception as e:
            return HttpResponse(e)

    def delete(self, request):
        try:
            params = QueryDict(request.body)
            print(params["house"], request.user.id)
            favorite = UserFavorites.objects.get(user_id=int(request.user.id), house_id=int(params["house"]))
            favorite.delete()
            return JsonResponse({'success': 1})
        except Exception as e:
            print(e)
            return JsonResponse({'success': 0})


class PopularView(View):
    def get(self, request):
        popular = HouseVisited.objects.values('house').annotate(Count('house')).order_by()
        return render(request, "houseTemplate.html", {'object_list': popular[:2]})
