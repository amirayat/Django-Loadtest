import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from countries.models import Country
from countries.serializers import CountryModelSerializer
from countries.psycopg_api import get_countries


class CountryListViewSet(ReadOnlyModelViewSet):
    """
    RESTful API view class to list countries
    """
    serializer_class = CountryModelSerializer
    queryset = Country.objects.all()


@api_view(['GET'])
def list_countries(request):
    countries = get_countries()
    return Response(countries)


@api_view(['GET'])
def cpu_bound_task(request):
    """
    dummy operation to create a cpu-bound task
    """
    total = int()
    for i in range(1, 10000):
        for j in range(1, 10000):
            total += i * j
    return Response({"final is:":total})