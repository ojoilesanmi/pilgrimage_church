from django.urls import path

from . import views

from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('better_nigeria', views.better_nigeria, name='better_nigeria'),
    path('registration', views.registration, name='registration')
    
]
