from django.conf.urls import url

from . import views

app_name = 'house'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # house/12
    url(r'^favorites/$', views.FavoritesView.as_view(), name='favorites'),
    url(r'^popular/$', views.PopularView.as_view(), name='popular'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailsViews.as_view(), name='details')
]
