from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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

    @method_decorator(cache_page(60*60*2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@api_view(['GET'])
def list_countries(request):
    countries = get_countries()
    return Response(countries)