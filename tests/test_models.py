from django.test import TestCase
from apps.directories.models import Status, Type, Category, Subcategory
from apps.transactions.models import Transaction
from django.core.exceptions import ValidationError
from decimal import Decimal

class StatusModelTest(TestCase):
    def test_create_status(self):
        status = Status.objects.create(name="Тестовый", order=1)
        self.assertEqual(status.name, "Тестовый")
        self.assertEqual(str(status), "Тестовый")

class TransactionModelTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name="Бизнес")
        self.type = Type.objects.create(name="Списание")
        self.category = Category.objects.create(name="Тест", type=self.type)
        self.subcategory = Subcategory.objects.create(name="Подтест", category=self.category)
    
    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            date="2024-01-01",
            status=self.status,
            type=self.type,
            category=self.category,
            subcategory=self.subcategory,
            amount=Decimal("1000.00"),
            comment="Тест"
        )
        self.assertEqual(transaction.amount, Decimal("1000.00"))
        self.assertEqual(str(transaction), "2024-01-01 | Списание | Тест | 1000.00₽")
    
    def test_validation_error_wrong_category(self):
        wrong_type = Type.objects.create(name="Пополнение")
        with self.assertRaises(ValidationError):
            Transaction.objects.create(
                date="2024-01-01",
                status=self.status,
                type=wrong_type,
                category=self.category,
                amount=Decimal("1000.00")
            )