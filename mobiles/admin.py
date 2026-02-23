from django.contrib import admin
from .models import Mobile

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'ram', 'storage']
    list_filter = ['brand', 'ram']
    search_fields = ['name', 'brand']
