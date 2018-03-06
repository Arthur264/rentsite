from helpers.objects import get_or_None, filter_or_None
from .models import House, HouseImage, HouseDetails
from authentication.models import User, UserProfile, Role
from django.views.generic import CreateView, DeleteView, ListView


# Create your views here.


class IndexView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return House.objects.all()

    def get_context_data(self, **kwargs):
        content = super(IndexView, self).get_context_data(**kwargs)
        content['agents'] = filter_or_None(UserProfile, user_role=Role.objects.get(name="Agent").pk)
        content['agents']['tex'] = "dsfh"
        for item in  content['agents']:
            print (get_or_None(User, pk= str(item.user_id)))
        return content


class DetailsViews(DeleteView):
    template_name = 'details.html'
    model = House

    def get_context_data(self, **kwargs):
        content = super(DetailsViews, self).get_context_data(**kwargs)
        content['imagehouse'] = filter_or_None(HouseImage, house=content["house"].pk)
        content['housedetails'] = get_or_None(HouseDetails, house=content["house"].pk)
        return content
