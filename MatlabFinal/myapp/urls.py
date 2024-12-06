
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [

    path('index/', views.index,name='index'),
    path('services/', views.services,name='services'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('myservices/', views.myservices,name='myservices'),
    path('doctors/', views.doctors,name='doctors'),
    path('departments/', views.departments,name='departments'),
    path('contact/', views.contact,name='contact'),
    path('appointment/', views.appointment,name='appointment'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete,),
    path('wow/', views.wow,name='wow'),
    path('dele/<int:id>', views.dele,),
    path('edit/<int:id>', views.edit,name='edit'),
    path('update/<int:id>', views.update,name='update'),
    path('login/', views.login, name='login'),
    path('', views.register, name='register'),
    path('uploadimage', views.upload_image, name='upload'),
    path('showimage', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

]
