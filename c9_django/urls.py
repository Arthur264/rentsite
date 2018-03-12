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
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^house/', include('buildings.urls')),
                  url(r'^agent/', include('agents.urls')),
                  url(r'^auth/', include('authentication.urls')),
                  url(r'^properties/', include('properties.urls')),
                  url(r'^profile/', include('profile.urls')),
                  url(r'^news/', include('news.urls')),
                  url(r'^gallery/', include('gallery.urls')),
                  url(r'^contact/', include('contact.urls')),
                  url(r'^search/', include('search.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
