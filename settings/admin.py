from django.contrib import admin

from settings.models import BackgroundImageModel, CategoryModel, ContactModel, ImageModel, NavbarModel, Products

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(NavbarModel)
admin.site.register(ImageModel)
admin.site.register(Products)
admin.site.register(BackgroundImageModel)
admin.site.register(ContactModel)
