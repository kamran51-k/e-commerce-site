from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, BooleanField, CharField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
class NavbarModel(models.Model):
    navbar_id = IntegerField()
    title = CharField(max_length=100,null=True,blank=True)
    category = BooleanField()

class CategoryModel(models.Model):
    style_id = IntegerField()
    style = CharField(max_length=100,null=True,blank=True)
    
class ImageModel(models.Model):
    background_image = models.ImageField(upload_to='image',null=True,blank=True)