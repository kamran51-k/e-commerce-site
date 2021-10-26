from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, URLField


# Create your models here.
class NavbarModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.BooleanField(default=False)
    slice = models.IntegerField(null=True,blank=True)
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
    category = models.ForeignKey(CategoryModel, on_delete=CASCADE, blank=True, null=True, related_name="products")
    image = models.ImageField(upload_to = "products/", null=True, blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)
    delete_price = models.FloatField(null=True,blank=True)

class BackgroundImageModel(models.Model):
    sale = models.CharField(max_length=100,null=True,blank=True)
    image_text = models.CharField(max_length=100,null=True,blank=True)
    background_image = models.ImageField(upload_to='images_folder',null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)

class ImageModel(models.Model):
    images = models.ImageField(upload_to="images_folder",null=True,blank=True)
    sale = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    
