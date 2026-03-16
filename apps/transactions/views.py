from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Transaction
from apps.directories.models import Category, Subcategory

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/list.html'
    context_object_name = 'transactions'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Фильтрация по дате
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        
        # Фильтрация по статусу
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status_id=status)
        
        # Фильтрация по типу
        type_id = self.request.GET.get('type')
        if type_id:
            queryset = queryset.filter(type_id=type_id)
        
        # Фильтрация по категории
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category_id=category)
        
        # Фильтрация по подкатегории
        subcategory = self.request.GET.get('subcategory')
        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Сохраняем параметры фильтрации для формы
        context['filters'] = self.request.GET.dict()
        return context

class TransactionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Transaction
    fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
    template_name = 'transactions/create.html'
    success_url = reverse_lazy('transactions:list')
    success_message = 'Транзакция успешно создана'

class TransactionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transaction
    fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
    template_name = 'transactions/edit.html'
    success_url = reverse_lazy('transactions:list')
    success_message = 'Транзакция успешно обновлена'

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'transactions/delete.html'
    success_url = reverse_lazy('transactions:list')
    success_message = 'Транзакция удалена'

# API views для динамических фильтров
def get_categories(request):
    type_id = request.GET.get('type_id')
    if type_id:
        categories = Category.objects.filter(type_id=type_id).values('id', 'name')
        return JsonResponse(list(categories), safe=False)
    return JsonResponse([], safe=False)

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    if category_id:
        subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
        return JsonResponse(list(subcategories), safe=False)
    return JsonResponse([], safe=False)