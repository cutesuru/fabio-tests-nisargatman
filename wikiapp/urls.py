from django.urls import path
import uuid
from .views import ContinentDetailView,ContinentListView,ContinentCreateView,ContinentUpdateView,ContinentDeleteView
from .views import CountryDetailView,CountryListView,CountryCreateView,CountryUpdateView,CountryDeleteView
from .views import CityDetailView,CityListView,CityCreateView,CityUpdateView,CityDeleteView
app_name = 'wikiapp'
urlpatterns = [
    # first five path are for Continent
    path("continent/", view=ContinentListView.as_view(), name="continent_list"),
    path("continent/add/",view=ContinentCreateView.as_view(),name="continent_create"),
    path("continent/<uuid:uuid>/", view=ContinentDetailView.as_view(), name="continent_detail"),
    path("continent/<uuid:uuid>/update/",view=ContinentUpdateView.as_view(),name='continent_update'),
    path("continent/<uuid:uuid>/delete/",view=ContinentDeleteView.as_view(),name='continent_delete'),
    # first five path are for country
    path("country/", view=CountryListView.as_view(), name="country_list"),
    path("country/add/",view=CountryCreateView.as_view(),name="country_create"),
    path("country/<uuid:uuid>/", view=CountryDetailView.as_view(), name="country_detail"),
    path("country/<uuid:uuid>/update/",view=CountryUpdateView.as_view(),name='country_update'),
    path("country/<uuid:uuid>/delete/",view=CountryDeleteView.as_view(),name='country_delete'),
    # first five path are for City
    path("city/", view=CityListView.as_view(), name="city_list"),
    path("city/add/",view=CityCreateView.as_view(),name="city_create"),
    path("city/<uuid:uuid>/", view=CityDetailView.as_view(), name="city_detail"),
    path("city/<uuid:uuid>/update/",view=CityUpdateView.as_view(),name='city_update'),
    path("city/<uuid:uuid>/delete/",view=CityDeleteView.as_view(),name='city_delete')
]
