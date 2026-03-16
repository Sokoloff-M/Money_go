from django.contrib import admin
from .models import Status, Type, Category, Subcategory

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'order']
    list_filter = ['type']
    ordering = ['type__order', 'order']
    inlines = [SubcategoryInline]

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_filter = ['category__type', 'category']