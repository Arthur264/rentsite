from django.conf.urls import url
from .views import IndexView, FavoritesView

app_name = "profile"
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^favorites/$', FavoritesView.as_view(), name="favorites"),
]
