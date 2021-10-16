from django.contrib import admin

from settings.models import CategoryModel, ImageModel, NavbarModel, Products

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(NavbarModel)
admin.site.register(ImageModel)
admin.site.register(Products)
