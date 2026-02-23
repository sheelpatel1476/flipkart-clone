from django.contrib import admin
from .models import FashionItem

@admin.register(FashionItem)
class FashionItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'price', 'size']
    list_filter = ['category', 'brand']
    search_fields = ['name', 'brand']
