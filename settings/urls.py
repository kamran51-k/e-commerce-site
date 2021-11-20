from django.urls import path
from .views import  home_view,category_filter_view,contact_view
urlpatterns = [
    path('',home_view,name='home_page'),
    path('category_filter/<int:navbar_id>/',category_filter_view, name='category_filter_page'),
    path('contact/',contact_view,name='contact_page'),
    
]


