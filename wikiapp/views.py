from .models import Continent,Country,City
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import CityForm,CountryForm,ContinentForm
from django.contrib import messages
from .task import create_continent,create_country,create_city
from django.shortcuts import redirect
import json
from django.db import transaction
import jsonpickle
""" Six class based views used to perform CRUD operation on Continent,Country and City """

""" List the continent names """
class ContinentListView(ListView):
      model = Continent

""" Detail View about Continent """
class ContinentDetailView(DetailView):
      model = Continent
    
      def get_object(self, queryset=None):
          return Continent.objects.get(uuid=self.kwargs.get("uuid"))      

""" Registering Details about the Continent"""

class ContinentCreateView(CreateView):
      model = Continent
      form_class= ContinentForm

      def form_valid(self, form):
          form.instance.creator = self.request.user
          data=form.cleaned_data
          print(data) 
          create_continent.delay(data)
          #messages.success(self.request, 'We are generating continent')
          return super().form_valid(form)

""" Option to update the details"""
class ContinentUpdateView(UpdateView):
    
      model = Continent
      form_class= ContinentForm
      @transaction.atomic()
      def form_valid(self, form):
          form.instance.creator = self.request.user
          data=form.cleaned_data
          print(data) 
          create_continent.delay(data)
          #messages.success(self.request, 'We are generating continent')
          return super().form_valid(form)
      
      @transaction.atomic()
      def get_object(self, queryset=None):
          return Continent.objects.get(uuid=self.kwargs.get("uuid")) 
      
      action='Update'

""" Delete the current Continent info from the DB"""

class ContinentDeleteView(DeleteView):

      model = Continent
      success_url =reverse_lazy('wikiapp:continent_list')
      @transaction.atomic()
      def get_object(self, queryset=None):
          return Continent.objects.get(uuid=self.kwargs.get("uuid"))

""" Overview about the Country """
class CountryListView(ListView):
      model = Country

"""Detail Information about the Country"""
class CountryDetailView(DetailView):
      model = Country
      
      def get_object(self, queryset=None):
          return Country.objects.get(uuid=self.kwargs.get("uuid"))      

"""Adding contents about the Country"""
class CountryCreateView(CreateView):
      model = Country
      form_class= CountryForm

      def form_valid(self, form):
          form.instance.creator = self.request.user
          data=form.cleaned_data
          print(data,"Country")
          data=jsonpickle.encode(data, unpicklable=False)
          print(data,"Country")
          create_country.delay(data)
          print("Checkpoint")
          return super().form_valid(form)

"""Updating the Country Content""" 
class CountryUpdateView(UpdateView):
      model = Country
      form_class= CountryForm

      @transaction.atomic()
      def form_valid(self, form):
          form.instance.creator = self.request.user
          data=form.cleaned_data
          data=jsonpickle.encode(data, unpicklable=False)
          create_country.delay(data)
          #messages.success(self.request, 'We are generating continent')
          return super().form_valid(form)

      @transaction.atomic()
      def get_object(self, queryset=None):
          return Country.objects.get(uuid=self.kwargs.get("uuid"))      
      action='Update'

"""Delete the specific country"""

class CountryDeleteView(DeleteView):

      model = Country
      success_url =reverse_lazy('wikiapp:country_list')
      @transaction.atomic()
      def get_object(self, queryset=None):
          return Country.objects.get(uuid=self.kwargs.get("uuid"))

"""Overview of the Cities"""
class CityListView(ListView):
      model = City

"""Detail about the City"""
class CityDetailView(DetailView):
      model = City
    
      def get_object(self, queryset=None):
          return City.objects.get(uuid=self.kwargs.get("uuid"))      

""" Register new City """
class CityCreateView(CreateView):
      model = City
      form_class= CityForm

      def form_valid(self, form):
          form.instance.creator = self.request.user
          data=form.cleaned_data
          print(data)
          data=jsonpickle.encode(data, unpicklable=False) 
          create_city.delay(data)
          return super().form_valid(form) 

""" Update the City Content """
class CityUpdateView(UpdateView):
    
      model = City
      form_class= CityForm
      @transaction.atomic()
      def form_valid(self, form):
          form.instance.creator = self.request.user
          data=form.cleaned_data
          print(data) 
          data=jsonpickle.encode(data, unpicklable=False)
          create_city.delay(data)
          return super().form_valid(form) 
      
      @transaction.atomic()
      def get_object(self, queryset=None):
          return City.objects.get(uuid=self.kwargs.get("uuid"))
      action='Update'

""" Delete the specific City """
class CityDeleteView(DeleteView):

      model = City
      success_url =reverse_lazy('wikiapp:city_list')
      @transaction.atomic()
      def get_object(self, queryset=None):
          return City.objects.get(uuid=self.kwargs.get("uuid"))       