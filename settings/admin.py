from django.contrib import admin

from settings.models import CategoryModel, ImageModel, NavbarModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(NavbarModel)
admin.site.register(ImageModel)