from django.conf.urls import url
from .views import IndexView, DetailsView, CommentView

app_name = "news"
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^commnent/$', CommentView.as_view(), name='comment'),
    url(r'^(?P<slug>[\w-]+)/$', DetailsView.as_view(), name='details')
]
