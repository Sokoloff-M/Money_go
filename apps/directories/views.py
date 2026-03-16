from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Status, Type, Category, Subcategory

# Статусы
class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'directories/status_list.html'
    context_object_name = 'statuses'

class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name', 'order']
    template_name = 'directories/forms/status_form.html'
    success_url = reverse_lazy('directories:status_list')
    success_message = 'Статус успешно создан'

class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name', 'order']
    template_name = 'directories/forms/status_form.html'
    success_url = reverse_lazy('directories:status_list')
    success_message = 'Статус успешно обновлен'

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'directories/status_confirm_delete.html'
    success_url = reverse_lazy('directories:status_list')
    success_message = 'Статус удален'

# Типы
class TypeListView(LoginRequiredMixin, ListView):
    model = Type
    template_name = 'directories/type_list.html'
    context_object_name = 'types'

class TypeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Type
    fields = ['name', 'order']
    template_name = 'directories/forms/type_form.html'
    success_url = reverse_lazy('directories:type_list')
    success_message = 'Тип успешно создан'

class TypeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Type
    fields = ['name', 'order']
    template_name = 'directories/forms/type_form.html'
    success_url = reverse_lazy('directories:type_list')
    success_message = 'Тип успешно обновлен'

class TypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Type
    template_name = 'directories/type_confirm_delete.html'
    success_url = reverse_lazy('directories:type_list')
    success_message = 'Тип удален'

# Категории
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'directories/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ['name', 'type', 'order']
    template_name = 'directories/forms/category_form.html'
    success_url = reverse_lazy('directories:category_list')
    success_message = 'Категория успешно создана'

class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = ['name', 'type', 'order']
    template_name = 'directories/forms/category_form.html'
    success_url = reverse_lazy('directories:category_list')
    success_message = 'Категория успешно обновлена'

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'directories/category_confirm_delete.html'
    success_url = reverse_lazy('directories:category_list')
    success_message = 'Категория удалена'

# Подкатегории
class SubcategoryListView(LoginRequiredMixin, ListView):
    model = Subcategory
    template_name = 'directories/subcategory_list.html'
    context_object_name = 'subcategories'

class SubcategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Subcategory
    fields = ['name', 'category', 'order']
    template_name = 'directories/forms/subcategory_form.html'
    success_url = reverse_lazy('directories:subcategory_list')
    success_message = 'Подкатегория успешно создана'

class SubcategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Subcategory
    fields = ['name', 'category', 'order']
    template_name = 'directories/forms/subcategory_form.html'
    success_url = reverse_lazy('directories:subcategory_list')
    success_message = 'Подкатегория успешно обновлена'

class SubcategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Subcategory
    template_name = 'directories/subcategory_confirm_delete.html'
    success_url = reverse_lazy('directories:subcategory_list')
    success_message = 'Подкатегория удалена'