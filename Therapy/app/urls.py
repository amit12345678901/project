from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('contact', views.submit_contact, name="contact"),
    path('contact_list', views.contact_list, name="contact_list"),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),  # Add this line
    path('appointment/', views.appointment_view, name='appointment'),
    path('appointments/', views.show_appointments, name='show_appointments'),
    path('appointments/edit/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),

]