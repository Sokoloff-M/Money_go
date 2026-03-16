from datetime import datetime, timedelta
from .models import Transaction

def get_transactions_summary(start_date=None, end_date=None):
    """Получить сводку по транзакциям за период"""
    queryset = Transaction.objects.all()
    
    if start_date:
        queryset = queryset.filter(date__gte=start_date)
    if end_date:
        queryset = queryset.filter(date__lte=end_date)
    
    summary = {
        'total_count': queryset.count(),
        'total_income': queryset.filter(type__name='Пополнение').aggregate(total=models.Sum('amount'))['total'] or 0,
        'total_expense': queryset.filter(type__name='Списание').aggregate(total=models.Sum('amount'))['total'] or 0,
        'balance': 0,
    }
    
    summary['balance'] = summary['total_income'] - summary['total_expense']
    return summary