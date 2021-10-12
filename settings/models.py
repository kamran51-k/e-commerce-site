from functools import cached_property
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH, BooleanField, CharField, IntegerField
from django.db.models.fields.files import ImageField
# Create your models here.
class NavbarModel(models.Model):
    title = CharField(max_length=100,null=True,blank=True)
    category = BooleanField()

class CategoryModel(models.Model):
    category_id = models.ManyToManyField('NavbarModel')
    style = CharField(max_length=100,null=True,blank=True)
    
class Products(models.Model):
    name = CharField(max_length=100,null=True,blank=True)
    

class ImageModel(models.Model):
    background_image = models.ImageField(upload_to='image',null=True,blank=True)