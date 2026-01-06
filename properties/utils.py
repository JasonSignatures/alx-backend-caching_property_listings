# properties/utils.py

from django.core.cache import cache
from .models import Property


def get_all_properties():
    """
    Fetch all properties from Redis cache if available,
    otherwise fetch from database and cache for 1 hour.
    """
    queryset = cache.get('all_properties')

    if queryset is None:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)  # cache for 1 hour

    return queryset
# properties/views.py

from django.shortcuts import render
from .utils import get_all_properties


def property_list(request):
    properties = get_all_properties()
    return render(request, 'properties/property_list.html', {
        'properties': properties
    })
