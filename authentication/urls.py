"""c9_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views

app_name = 'auth'
urlpatterns = [
    # url(r'^$/', admin.site.urls),
    url(r'^singUp/', views.SingUp.as_view(), name='singUp'),
    url(r'^singIn/', views.SingIn.as_view(), name='singIn'),
    url(r'^activate/(?P<userId>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.Activate.as_view(), name='activate'),
    url(r'^reset', views.Reset.as_view(), name="reset"),
    url(r'^logout', views.Logout.as_view(), name="logout"),
    url(r'^delete', views.Delete.as_view(), name="delete")
]
