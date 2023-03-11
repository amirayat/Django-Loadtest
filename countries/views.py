from rest_framework.viewsets import ReadOnlyModelViewSet
from countries.models import Country
from countries.serializers import CountryModelSerializer


class CountryListViewSet(ReadOnlyModelViewSet):
    """
    RESTful API view class to list countries
    """
    serializer_class = CountryModelSerializer
    queryset = Country.objects.all()
