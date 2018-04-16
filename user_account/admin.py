from django.contrib import admin
from .models import Company_Profile
'''from .models import CustomUser


@admin.register(CustomUser)
class customUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']'''


@admin.register(Company_Profile)
class Company_Profile_Admin(admin.ModelAdmin):
    list_display = ['companyName', 'contactNumber', 'emailAddress']
