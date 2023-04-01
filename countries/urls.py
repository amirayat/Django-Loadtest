from django.urls import include, path
from rest_framework import routers
from countries.views import CountryListViewSet, list_countries, cpu_bound_task


country_router = routers.SimpleRouter()
country_router.register(r'', CountryListViewSet)


urlpatterns = [ 
    path('calculate/', cpu_bound_task),
    path('raw/', list_countries),
    path('', include(country_router.urls)),
]