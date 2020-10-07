from django.contrib import admin
from django.urls import path
from . import views
admin.site.site_header = "Data Scientist Shahid     "
admin.site.site_title = "Artificial Intillegence"
admin.site.index_title = "Welcome to Data Scientist Researcher Portal"

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('carrier', views.carrier, name='carrier'),
]
