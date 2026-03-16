from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from apps.directories.models import Status, Type, Category, Subcategory

class Transaction(models.Model):
    date = models.DateField('Дата операции')
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name='Статус'
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        verbose_name='Тип'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория'
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        verbose_name='Подкатегория',
        null=True,
        blank=True
    )
    amount = models.DecimalField(
        'Сумма',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    comment = models.TextField(
        'Комментарий',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )
    
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return f"{self.date} | {self.type} | {self.category} | {self.amount}₽"
    
    def clean(self):
        # Проверка: категория должна относиться к выбранному типу
        if self.category and self.category.type != self.type:
            raise ValidationError(
                f'Категория "{self.category}" не относится к типу "{self.type}"'
            )
        
        # Проверка: подкатегория должна относиться к выбранной категории
        if self.subcategory and self.subcategory.category != self.category:
            raise ValidationError(
                f'Подкатегория "{self.subcategory}" не относится к категории "{self.category}"'
            )
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)