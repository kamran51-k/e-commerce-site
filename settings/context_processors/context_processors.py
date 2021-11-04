from django.shortcuts import render
from settings.models import NavbarModel,CategoryModel

def header(request):
    context = {}
    navbar_queryset = NavbarModel.objects.all()
    category_queryset = CategoryModel.objects.all()
    context['category_queryset'] = category_queryset
    context['navbar_queryset'] = navbar_queryset
    return context