from django.db import models
import uuid
from django.urls import reverse


class TimeStampedModel(models.Model):
      """
      An abstract base class model that provides selfupdating ``created`` and ``modified`` fields.
      """
      created = models.DateTimeField(auto_now_add=True)
      modified = models.DateTimeField(auto_now=True)
      class Meta:
            abstract = True

"""Continent model
      Attributes:
          1)uuid:PK
          2)name:STRING
          3)population:INT
          4)area_in_sq_meters:INT
"""
class Continent(TimeStampedModel):
      uuid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
      name=models.CharField(max_length=100,unique=True)
      population=models.IntegerField(null=False)
      area_in_sq_meters = models.FloatField(unique=False, null=False)

      def __str__(self):
        return f"{self.name}"

      def get_absolute_url(self):
          return reverse("wikiapp:continent_detail", kwargs={"uuid": self.uuid})

"""Country model
      Attributes:
          1)uuid:PK
          2)name:String
          3)population:INT
          4)area_in_sq_meters:INT
          5)created_At:DataTime
          6)updated_At:DateTime
          7)Number of hospitals:INT
          8)Number of national parks:INT
"""
class Country(TimeStampedModel):
      uuid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
      name = models.CharField(max_length=100,unique=True)
      population = models.IntegerField(null=False)
      area_in_sq_meters = models.FloatField(unique=False, null=False)
      number_of_hospitals = models.IntegerField(null=False)
      number_of_national_parks = models.IntegerField(null=False)
      continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

      def __str__(self):
          return f"{self.name}"
      
      def get_absolute_url(self):
          return reverse("wikiapp:country_detail", kwargs={"uuid": self.uuid})


"""City model
      Attributes:
          1)uuid:PK
          2)name:String
          3)population:INT
          4)area_in_sq_meters:INT
          5)created_At:DataTime
          6)updated_At:DateTime
          7)Number of roads:INT
          8)Number of trees:INT
"""
class City(TimeStampedModel):
      uuid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
      name = models.CharField(max_length=100,unique=True)
      population = models.IntegerField(null=False)
      area_in_sq_meters = models.FloatField(unique=False, null=False)
      number_of_roads = models.IntegerField(unique=False, null=True)
      number_of_trees = models.IntegerField(unique=False, null=True)
      country = models.ForeignKey(Country, on_delete=models.CASCADE)
      
      def __str__(self):
          return f"{self.name}"

      def get_absolute_url(self):
          return reverse("wikiapp:city_detail", kwargs={"uuid": self.uuid})
      
	
