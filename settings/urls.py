from django.urls import path
from .views import  home_view,category_filter_view, product_view
urlpatterns = [
    path('',home_view,name='home_page'),
    path('category_filter/<int:navbar_id>/',category_filter_view, name='category_filter_page'),
    path('product_filter/<int:category_id>/',product_view,name='product_page'),
    
]


