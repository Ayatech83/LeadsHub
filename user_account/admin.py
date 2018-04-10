from django.contrib import admin
from .models import CustomUser, userCategories


@admin.register(CustomUser)
class customUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']

@admin.register(userCategories)
class userCategoriesAdmin(admin.ModelAdmin):
    list_display = ['userId', 'catId']
