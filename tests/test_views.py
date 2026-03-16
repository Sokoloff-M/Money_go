from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.directories.models import Status, Type

class TransactionViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        
        self.status = Status.objects.create(name="Бизнес")
        self.type = Type.objects.create(name="Списание")
    
    def test_list_view(self):
        response = self.client.get(reverse('transactions:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/list.html')
    
    def test_create_view(self):
        response = self.client.get(reverse('transactions:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/create.html')