from django_filters import FilterSet
from django_filters import rest_framework as filters
from .models import House

class HouseFilter(FilterSet):
    min_price = filters.NumberFilter(name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(name="area", lookup_expr='gte')
    max_area = filters.NumberFilter(name="area", lookup_expr='lte')
    bathrooms = filters.NumberFilter(name="bathrooms")
    bedrooms = filters.NumberFilter(name="bedrooms")
    class Meta:
        model = House
        fields = ['status','min_price', 'max_price', 'bedrooms', 'bathrooms','max_area', 'min_area']