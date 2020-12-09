from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BetterNigeriaRegistration
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'church/index.html')

def better_nigeria(request):
    return render(request, 'church/better.html')
    
def about(request):
    return render(request, 'church/about.html')

def contact(request):
    return render(request, 'church/contact.html')
    
def messages(request):
    return render(request, 'church/messages.html')

def registration(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        registration = BetterNigeriaRegistration(fullname=fullname, email=email, phone_number=phone_number)
        registration.save()
        messages.success(request, "Thank you for registering we will be in touch shortly")
        return redirect('registration')
    else:
    
        return render(request, 'church/registration.html')
   
