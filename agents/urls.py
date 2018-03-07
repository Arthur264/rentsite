from django.conf.urls import url

from . import views
app_name = 'agent'
urlpatterns = [
    url(r'$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<username>[\w-]+)/$', views.DetailsViews.as_view(), name='details')
]