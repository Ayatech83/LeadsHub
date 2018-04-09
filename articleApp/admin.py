from django.contrib import admin
from .models import articles

@admin.register(articles)
class articlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher']