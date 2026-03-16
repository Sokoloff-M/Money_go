from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='list'),
    path('create/', views.TransactionCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='delete'),
    
    # API endpoints для динамических фильтров
    path('api/get-categories/', views.get_categories, name='get_categories'),
    path('api/get-subcategories/', views.get_subcategories, name='get_subcategories'),
]