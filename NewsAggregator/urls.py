
from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('trending/', views.index1),
    path('homeaffairs/', views.index2),
    path('fa/', views.index3),
    path('sports/', views.index4),
    path('snt/', views.index5),
    path('busi/', views.index6),
    path('dtu/', views.index7)       
 ]
