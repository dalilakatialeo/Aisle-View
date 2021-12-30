from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()), #users
    path('users/<int:pk>/', views.CustomUserDetail.as_view()), #/users/id
]

urlpatterns = format_suffix_patterns(urlpatterns)