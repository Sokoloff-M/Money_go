from django.db import models

class Status(models.Model):
    """Справочник статусов"""
    name = models.CharField('Название', max_length=50, unique=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Type(models.Model):
    """Справочник типов"""
    name = models.CharField('Название', max_length=50, unique=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Category(models.Model):
    """Категория, привязанная к типу"""
    name = models.CharField('Название', max_length=100)
    type = models.ForeignKey(
        Type, 
        on_delete=models.CASCADE,
        verbose_name='Тип',
        related_name='categories'
    )
    order = models.PositiveIntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['type__order', 'order', 'name']
        unique_together = ['name', 'type']
    
    def __str__(self):
        return f"{self.name} ({self.type.name})"

class Subcategory(models.Model):
    """Подкатегория, привязанная к категории"""
    name = models.CharField('Название', max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='subcategories'
    )
    order = models.PositiveIntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['category__order', 'order', 'name']
        unique_together = ['name', 'category']
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"