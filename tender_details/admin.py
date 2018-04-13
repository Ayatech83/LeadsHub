from django.contrib import admin
from .models import tender

@admin.register(tender)
class tenderAdmin(admin.ModelAdmin):
    list_display = ['buyersName', 'refNum', 'issueDate', 'closingDate']


#@admin.register(category)
#class categoryAdmin(admin.ModelAdmin):
    #list_display = ['catCode', 'catDescription']
