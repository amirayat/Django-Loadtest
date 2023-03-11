from rest_framework.serializers import ModelSerializer
from countries.models import Country


class CountryModelSerializer(ModelSerializer):
    """
    serializer for countries
    """

    class Meta:
        model = Country
        fields = '__all__'