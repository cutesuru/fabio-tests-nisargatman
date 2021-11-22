import string
from .models import Continent,Country,City
from celery import shared_task
""" async Continent creation and updation """
@shared_task
def create_continent(data):
    print(data)
    Continent.objects.create(name=data['name'], population=data['population'], area_in_sq_meters=data['area_in_sq_meters'])
    return '{} continent data created with success!'.format (data)

""" async Country creation and updation """
@shared_task
def create_country(data):
    print(data)
    Country.objects.create(name=data['name'], population=data['population'], area_in_sq_meters=data['area_in_sq_meters'],number_of_hospitals=data['number_of_hospitals'],number_of_national_parks=data['number_of_national_parks'],continent=data['continent'])
    return '{} country data created with success!'.format (data)

""" async City creation and updation """
@shared_task
def create_city(data):
    print(data)
    City.objects.create(name=data['name'], population=data['population'], area_in_sq_meters=data['area_in_sq_meters'],number_of_roads=data['number_of_roads'],number_of_trees=data['number_of_trees'],country=data['country'])
    return '{} city data created with success!'.format (data)
