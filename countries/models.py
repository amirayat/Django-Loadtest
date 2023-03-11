from django.db import models


class Country(models.Model):
    """
    class model for world countries
    """
    name = models.CharField(max_length=36)
    iso3 = models.CharField(max_length=3)
    iso2 = models.CharField(max_length=2)
    numeric_code = models.CharField(max_length=3)
    phone_code = models.CharField(max_length=16)
    capital = models.CharField(max_length=20, null=True)
    currency = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=39)
    currency_symbol = models.CharField(max_length=6)
    tld = models.CharField(max_length=3)
    native = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=8, null=True)
    subregion = models.CharField(max_length=25, null=True)
    timezones = models.JSONField(default=list)
    translations = models.JSONField(null=True)
    latitude = models.CharField(max_length=12)
    longitude = models.CharField(max_length=13)
    emoji = models.CharField(max_length=2)
    emojiU = models.CharField(max_length=15)

    class Meta:
        db_table = 'countries'
