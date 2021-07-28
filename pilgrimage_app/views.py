from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import BetterNigeriaRegistration
from .models import Contact
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

def ministries(request):
    return render(request, 'church/ministries.html')

def church(request):
    return render(request, 'church/church.html')
    
# def messages(request):
#     return render(request, 'church/messages.html')

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

def messages(request):
    # obj = get_object_or_404(Song, id=id)

    # context = {
    #     'object': obj,
    # }

    return render(request, 'church/messages.html')

def contact_us(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
    
        
        contact = Contact(fullname=fullname, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'You have succesfully submitted your message. We will be in touch with you shortly')

        return redirect('index')

   
