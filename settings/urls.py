from django.urls import path
from .views import home_view,category_filter_view,sub_filter_view
urlpatterns = [
    path('',home_view,name='home_page'),
    path('category_filter/<int:navbar_id>/',category_filter_view, name='category_filter_page'),
    path('sub_filter/<int:sub_id>/',sub_filter_view, name='sub_filter_page'),
]


