from django.shortcuts import render

from settings.models import CategoryModel, ImageModel, NavbarModel

# Create your views here.
def home_view(request):
    context ={}
    navbar_queryset = NavbarModel.objects.all()
    image_queryset = ImageModel.objects.all()
    category_queryset = CategoryModel.objects.all()
    context['category_queryset'] = category_queryset
    context['navbar_queryset'] = navbar_queryset
    context['image_queryset'] = image_queryset
    
    return render(request,'index.html',context)


def category_filter_view(request,navbar_id):
    context = {}
    categories = CategoryModel.objects.filter(category_id=navbar_id)
    context['categories'] = categories
    return render(request,'category_filter.html', context)
