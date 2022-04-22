from django_filters import rest_framework as filters
from django.db.models import Q


from .models import UserBmiInfo

def filter_by_status_types(queryset, name, value):
    values = value.split(',')
    return queryset.filter(status__in=values)

class BMIInfoFilter(filters.FilterSet):
    status_type = filters.CharFilter(method=filter_by_status_types)
    class Meta:
        model = UserBmiInfo
        fields = ['status_type']
