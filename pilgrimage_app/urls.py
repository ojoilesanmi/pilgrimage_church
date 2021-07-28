from django.urls import path

from . import views

from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('better_nigeria', views.better_nigeria, name='better_nigeria'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('sermon', views.sermon, name='sermon'),
    path('registration', views.registration, name='registration'),
    path('ministries', views.ministries, name='ministries'),
    path('church', views.church, name='church'),
    
]
