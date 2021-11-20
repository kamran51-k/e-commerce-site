from django.contrib import admin

from settings.models import BackgroundImageModel, CategoryModel, ClientBrandModel, ContactUsModel, CreatorModel, ImageModel, NavbarModel, Products, CreatorModel, ContactModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(NavbarModel)
admin.site.register(ImageModel)
admin.site.register(Products)
admin.site.register(BackgroundImageModel)
admin.site.register(CreatorModel)
admin.site.register(ContactModel)
admin.site.register(ClientBrandModel)
admin.site.register(ContactUsModel)


