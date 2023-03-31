from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from countries.models import Country
from countries.serializers import CountryModelSerializer
from countries.pymongo_api import get_countries


class CountryListViewSet(ReadOnlyModelViewSet):
    """
    RESTful API view class to list countries
    using orm
    """
    serializer_class = CountryModelSerializer
    queryset = Country.objects.all()


@api_view(['GET'])
def list_countries(request):
    """
    RESTful API view function to list countries
    raw mongo query
    """
    countries = get_countries()
    return Response(countries)