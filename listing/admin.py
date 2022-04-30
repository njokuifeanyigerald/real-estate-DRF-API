from django.contrib import admin
from .models import ListingModel


class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'realtor', 'title', 'slug']
    list_display_links = ['id', 'realtor', 'title', 'slug']
    list_filter = ['realtor' ]
    list_per_page = 20
    search_fields = ['title', 'description', 'realtor']







admin.site.register(ListingModel, ListingAdmin)