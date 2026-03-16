import django_filters
from .models import Transaction
from apps.directories.models import Status, Type, Category, Subcategory

class TransactionFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    type = django_filters.ModelChoiceFilter(queryset=Type.objects.all())
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    subcategory = django_filters.ModelChoiceFilter(queryset=Subcategory.objects.all())
    
    class Meta:
        model = Transaction
        fields = ['date_from', 'date_to', 'status', 'type', 'category', 'subcategory']