from django.conf.urls import url

from . import views
app_name = 'agent'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailsViews.as_view(), name='details')
]