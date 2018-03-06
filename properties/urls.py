from django.conf.urls import url
from .views import IndexView, Card

app_name = 'properties'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^card/$', Card.as_view(), name='card')
]