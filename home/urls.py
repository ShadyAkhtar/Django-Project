from django.contrib import admin
from django.urls import path
from home import views


# added by shadab
#Django admin portal 
admin.site.site_header = "Shades Of Ice"
admin.site.site_title = "Shades Of Ice Admin Portal"
admin.site.index_title = "Welcome to Shades Of Ices Admin Portal"

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
]
