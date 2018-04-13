from django.contrib import admin
from .models import CustomUser, category


@admin.register(CustomUser)
class customUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['catCode', 'catDescription']
