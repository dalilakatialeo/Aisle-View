from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('products/', views.Product.as_view()), #products
    path('product-list/<int:pk>/', views.CustomUserDetail.as_view()), #/users/id
]

urlpatterns = format_suffix_patterns(urlpatterns)