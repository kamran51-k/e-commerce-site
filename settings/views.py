from django.http import request
from django.shortcuts import render, redirect



from settings.models import CategoryModel, BackgroundImageModel, ClientBrandModel, ContactUsModel, CreatorModel, ImageModel,NavbarModel, Products, ContactModel

# Create your views here.
def home_view(request):
    context ={}
    navbar_queryset = NavbarModel.objects.all()
    category_queryset = CategoryModel.objects.all()
    product_queryset = Products.objects.all()
    backgroundimage_queryset = BackgroundImageModel.objects.all()
    image_queryset = ImageModel.objects.all()
    creator_queryset = CreatorModel.objects.all()
    client_brand_queryset = ClientBrandModel.objects.all()
    contact_us_view = ContactUsModel.objects.all()
    # products = Products.objects.filter(product_id=category_id)
    # context['products'] = products
    context['category_queryset'] = category_queryset
    context['navbar_queryset'] = navbar_queryset
    context['product_queryset'] = product_queryset
    context['backgroundimage_queryset'] = backgroundimage_queryset
    context['image_queryset'] = image_queryset
    context['creator_queryset'] = creator_queryset
    context['client_brand_queryset'] = client_brand_queryset
    context['contact_us_view'] = contact_us_view
    if request.GET.get("category", None):
        context['product_queryset'] = context['product_queryset'].filter(category__style = request.GET.get("category"))
         
    return render(request,'index.html',context)


def category_filter_view(request,navbar_id):
    context = {}
    categories = CategoryModel.objects.filter(category_id=navbar_id)
    context['categories'] = categories
    return render(request,'category_filter.html', context)

# def product_view(request,category_id):
#     context={}
#     products = Products.objects.filter(product_id=category_id)
#     context['products'] = products
#     return render(request,'index.html',context)

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


def client_brand_view(request):
    context = {}
    client_brand_queryset = ClientBrandModel.objects.all()
    context['client_brand_queryset'] = client_brand_queryset
    return render(request, 'index.html', context)
 
