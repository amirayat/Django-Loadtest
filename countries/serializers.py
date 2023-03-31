from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from countries.models import Country


class CountryModelSerializer(ModelSerializer):
    """
    serializer for countries
    """
    timezones = serializers.JSONField()
    translations = serializers.JSONField()

    class Meta:
        model = Country
        exclude = ['_id']