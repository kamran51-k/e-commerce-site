from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, URLField


# Create your models here.
class NavbarModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

class CategoryModel(models.Model):
    url = URLField(null=True,blank=True)
    subcategory = models.BooleanField(default=False)
    category_id = models.ManyToManyField('NavbarModel')
    style = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.style}'
        
class Products(models.Model):
    name = CharField(max_length=100,null=True,blank=True)
    price = IntegerField(null=True,blank=True)

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images',null=True,blank=True)
    
