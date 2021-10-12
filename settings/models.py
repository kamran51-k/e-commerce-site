from django.db import models


# Create your models here.
class NavbarModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class CategoryModel(models.Model):
    category_id = models.ManyToManyField('NavbarModel')
    style = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.style}'


class Products(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)


class ImageModel(models.Model):
    background_image = models.ImageField(upload_to='image', null=True, blank=True)
