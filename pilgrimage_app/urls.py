from django.urls import path

from . import views

from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('better_nigeria', views.better_nigeria, name='better_nigeria'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('messages', views.messages, name='messages'),
    path('registration', views.registration, name='registration'),
    
]
