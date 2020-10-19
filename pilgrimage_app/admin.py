from django.contrib import admin
from .models import BetterNigeriaRegistration

class BetterNigeriaRegistrationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number')
    list_per_page = 25 


admin.site.register(BetterNigeriaRegistration, BetterNigeriaRegistrationAdmin)