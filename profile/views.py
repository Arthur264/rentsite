from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/house/'
    redirect_field_name = 'redirect_to'
    template_name = 'profile.html'


class FavoritesView(LoginRequiredMixin, TemplateView):
    login_url = '/house/'
    redirect_field_name = 'redirect_to'
    template_name = 'profilefavorites.html'