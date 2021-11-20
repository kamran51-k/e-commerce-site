from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, NullBooleanField, URLField
# Create your models here.
class NavbarModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.BooleanField(default=False)
    url = models.URLField()
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
    
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

class CreatorModel(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    profession = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=300, null=True, blank=True)
    photo = models.ImageField(upload_to="images_folder", null=True, blank=True)
    about = models.CharField(max_length=100, null=True, blank=True)

class ClientBrandModel(models.Model):
    photo = models.ImageField(upload_to = "images_folder", null = True, blank = True)
    alt_name = models.CharField(max_length=15, blank=True, null=True)

class ContactUsModel(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    adress = models.CharField(max_length=45, null=True, blank=True)
    number = models.IntegerField( null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank= True)
    wdigets = models.ImageField(upload_to = "images_folder", null=True, blank = True)
    widgets_url = models.URLField(max_length =100 ,null=True, blank=True)











