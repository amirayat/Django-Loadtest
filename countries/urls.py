from django.urls import include, path
from rest_framework import routers
from countries.views import CountryListViewSet


country_router = routers.SimpleRouter()
country_router.register(r'', CountryListViewSet)


urlpatterns = [ 
    path('', include(country_router.urls)),
]