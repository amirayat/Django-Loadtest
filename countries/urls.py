from django.urls import include, path
from rest_framework import routers
from countries.views import CountryListViewSet, list_countries


country_router = routers.SimpleRouter()
country_router.register(r'', CountryListViewSet)


urlpatterns = [ 
    path('raw/', list_countries),
    path('', include(country_router.urls)),
]