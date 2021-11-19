from django import forms
from django.core.exceptions import ValidationError
from .models import Country,Continent,City
"""
Validator to check the population and area of all countries of a continent less than or equal to continent population and area
"""
class CountryForm(forms.ModelForm):

    class Meta:
          model=Country
          fields=('name','population','area_in_sq_meters','number_of_hospitals','number_of_national_parks','continent')
    
    def clean(self):
        data=super(CountryForm,self).clean()
        print(data)
        number=self.cleaned_data.get('population')
        area=self.cleaned_data.get('area_in_sq_meters')
        continent=self.cleaned_data.get('continent')
        print(self.cleaned_data,continent)
        per_type=Continent.objects.get(name=continent)
        print(per_type)
        items = Country.objects.filter(continent=per_type)
        print(items)
        total_country_population=number
        val_population=0
        val_area=0
        total_country_area=area
        if(items is not None):
           for i in items:
               val_population+=i.population
               val_area+=i.population
        total_country_population+=val_population 
        total_country_area+=val_area 
        continent_population=per_type.population
        continent_area=per_type.area_in_sq_meters
        if(total_country_population>continent_population):
            raise ValidationError("Incorrect population value") 
        if(total_country_area>continent_area): 
            raise ValidationError("Incorrect area in sq meters value")     

"""
Validator to check the population and area of all cities of a country less than or equal to country population and area
"""
class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name','population','area_in_sq_meters','number_of_roads','number_of_trees','country')
    
    def clean(self):
        data=super(CityForm,self).clean()
        print(data)
        number=self.cleaned_data.get('population')
        area=self.cleaned_data.get('area_in_sq_meters')
        country=self.cleaned_data.get('country')
        print(self.cleaned_data,country)
        per_type=Country.objects.get(name=country)
        print(per_type)
        items = City.objects.filter(country=per_type)
        print(items)
        total_city_population=number
        val_population=0
        val_area=0
        total_city_area=area
        if(items is not None):
           for i in items:
               val_population+=i.population
               val_area+=i.population
        total_city_population+=val_population 
        total_city_area+=val_area 
        country_population=per_type.population
        country_area=per_type.area_in_sq_meters
        if(total_city_population>country_population):
            raise ValidationError("Incorrect population value") 
        if(total_city_area>country_area): 
            raise ValidationError("Incorrect area in sq meters value") 
           
