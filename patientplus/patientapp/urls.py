from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from patientapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('services/', views.services, name='services'),

]
