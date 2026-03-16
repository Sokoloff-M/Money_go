from django.contrib import admin
from django import forms
from .models import Transaction
from apps.directories.models import Category, Subcategory

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Динамическая фильтрация категорий по типу
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.type:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)
        
        # Динамическая фильтрация подкатегорий по категории
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.category:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    form = TransactionForm
    list_display = ['date', 'type', 'category', 'subcategory', 'amount', 'status']
    list_filter = ['type', 'status', 'category', 'date']
    search_fields = ['comment']
    date_hierarchy = 'date'
    ordering = ['-date']
    fieldsets = (
        ('Основная информация', {
            'fields': ('date', 'status', 'type', 'amount')
        }),
        ('Категоризация', {
            'fields': ('category', 'subcategory')
        }),
        ('Дополнительно', {
            'fields': ('comment',),
            'classes': ('collapse',)
        }),
    )
    
    class Media:
        js = ('js/transaction_admin.js',)