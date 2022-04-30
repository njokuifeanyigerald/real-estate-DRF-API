from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_realtor','email_verified', 'is_staff', 'is_superuser']
    list_display_links = ['id', 'username', 'email', 'is_realtor']
    list_filter = ['email', 'username', 'email_verified', 'is_realtor']
    list_per_page = 20
    search_fields = ['username', 'email', 'is_realtor', 'email_verified']

admin.site.register(User, UserAdmin)
