import django_filters
from django_filters import DateFilter
from .models import City


class CityFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    stop_date = DateFilter(field_name='date', lookup_expr='lte')
    class Meta:
        model = City
        fields = ['name']
