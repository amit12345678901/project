from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('contact', views.submit_contact, name="contact"),
    path('contact_list', views.contact_list, name="contact_list"),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),  # Add this line

]