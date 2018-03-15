import django_filters
from .models import House

class HouseFilter(django_filters.FilterSet):
    class Meta:
        model = House
        fields = ['status','price', 'bedrooms', 'bathrooms','area']