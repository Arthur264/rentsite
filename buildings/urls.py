from django.conf.urls import url

from . import views
app_name = 'house'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #house/12
    url(r'^(?P<slug>[\w-]+)/$', views.details, name='details')
]