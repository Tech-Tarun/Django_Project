from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('screen3',views.screen3,name='screen3'),
    path('delete/<id>',views.delete,name='delete'),
    path('edit/<id>',views.edit,name='edit'),
    path('logout',views.logout,name='logout'),
]