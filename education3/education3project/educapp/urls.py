from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('forms/',views.forms,name='forms'),
    path('new/',views.new,name='new'),
    path('logout/',views.logout,name='logout')
]