from django.conf.urls import url
from .views import IndexView

app_name = "profile"
urlpatterns = [
    url(r'$', IndexView.as_view(), name="index")
]