from django.http import request
from django.shortcuts import render

from settings.models import CategoryModel,NavbarModel, Products

# Create your views here.
def home_view(request):
    context ={}
    navbar_queryset = NavbarModel.objects.all()
    category_queryset = CategoryModel.objects.all()
    product_queryset = Products.objects.all()
    context['category_queryset'] = category_queryset
    context['navbar_queryset'] = navbar_queryset
    context['product_queryset'] = product_queryset

    if request.GET.get("category", None):
        context['product_queryset'] = context['product_queryset'].filter(category__style = request.GET.get("category"))
    

    
    return render(request,'index.html',context)


def category_filter_view(request,navbar_id):
    context = {}
    categories = CategoryModel.objects.filter(category_id=navbar_id)
    context['categories'] = categories
    return render(request,'category_filter.html', context)

def product_view(request,category_id):
    context={}
    products = Products.objects.filter(product_id=category_id)
    context['products'] = products
    return render(request,'product.html',context)