from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from userApp import views

urlpatterns = [
    path('getusers/', views.CustomUserList.as_view()),
    path('getuser/<int:pk>/', views.CustomUserDetail.as_view()),
] 

urlpatterns = format_suffix_patterns(urlpatterns)   