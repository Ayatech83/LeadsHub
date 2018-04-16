from django.contrib import admin
from .models import tender, category, provinces

@admin.register(tender)
class tenderAdmin(admin.ModelAdmin):
    list_display = ['buyersName', 'refNum', 'issueDate', 'closingDate']


@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['catCode', 'catDescription']

@admin.register(provinces)
class provincesAdmin(admin.ModelAdmin):
    list_display = ['id', 'provinceName']
