from django.contrib import admin
from .models import Category, Listing

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'price', 'location', 'status', 'created_at']
    list_filter = ['status', 'location', 'category']
    search_fields = ['title', 'description']