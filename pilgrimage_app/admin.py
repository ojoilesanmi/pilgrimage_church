from django.contrib import admin
from .models import BetterNigeriaRegistration
from .models import Messages
from . models import Contact

class BetterNigeriaRegistrationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number')
    list_per_page = 25 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'message', 'contact_date')
    list_per_page = 25

class MessagesAdmin(admin.ModelAdmin):
    list_display =('message_title', 'cloudinary_link')

admin.site.register(BetterNigeriaRegistration, BetterNigeriaRegistrationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Messages, MessagesAdmin)