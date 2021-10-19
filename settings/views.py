from django.http import request
from django.shortcuts import render

from settings.models import CategoryModel, ImageModel, NavbarModel, Products

# Create your views here.
def home_view(request):
    context ={}
    navbar_queryset = NavbarModel.objects.all()
    image_queryset = ImageModel.objects.all()
    category_queryset = CategoryModel.objects.all()
    product_queryset = Products.objects.all()
    context['category_queryset'] = category_queryset
    context['navbar_queryset'] = navbar_queryset
    context['image_queryset'] = image_queryset
    context['product_queryset'] = product_queryset
    
    return render(request,'index.html',context)


def category_filter_view(request,navbar_id):
    context = {}
    categories = CategoryModel.objects.filter(category_id=navbar_id)
    if len(categories) > 2:
        context['categories'] = categories[:2]
        context['and_more'] = "And more"
        return render(request, 'category_filter.html', context)
    context['categories'] = categories[:2]
    return render(request,'category_filter.html', context)

def sub_filter_view(request,sub_id):
    context = {}
    subcategories = CategoryModel.objects.filter(category_id=sub_id)[2:]
    context['subcategories'] = subcategories
    return render(request,'sub_filter.html',context)
