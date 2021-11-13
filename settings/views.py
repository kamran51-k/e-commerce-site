from django.http import request
from django.shortcuts import render, redirect



from settings.models import CategoryModel, BackgroundImageModel, CreatorModel, ImageModel,NavbarModel, Products

# Create your views here.
def home_view(request):
    context ={}
    navbar_queryset = NavbarModel.objects.all()
    category_queryset = CategoryModel.objects.all()
    product_queryset = Products.objects.all()
    backgroundimage_queryset = BackgroundImageModel.objects.all()
    image_queryset = ImageModel.objects.all()
    creator_queryset = CreatorModel.objects.all()
    context['category_queryset'] = category_queryset
    context['navbar_queryset'] = navbar_queryset
    context['product_queryset'] = product_queryset
    context['backgroundimage_queryset'] = backgroundimage_queryset
    context['image_queryset'] = image_queryset
    context['creator_queryset'] = creator_queryset
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
    return render(request,'index.html',context)

<<<<<<< Updated upstream
def contact_view(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        subject = request.POST.get('subject',None)
        message = request.POST.get('message',None)
        ContactModel.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        return redirect('home_page')
    else:
        return render(request,'contact.html',context) 
    return render(request,'contact.html',context)
def creator_view(request):
    context = {}
    creator_queryset = CreatorModel.objects.all()
    context['creator_queryset'] = creator_queryset
    return render(request, 'index.html',context)
=======
>>>>>>> Stashed changes
