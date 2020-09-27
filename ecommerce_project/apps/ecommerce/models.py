from django.db import models
from apps.users.models import User

# Create your models here.
class Person(models.Model):
  id = models.AutoField(primary_key = True)
  user_id =  models.ForeignKey(User, on_delete=models.RESTRICT)
  name = models.CharField(max_length = 200)
  last_name = models.CharField(max_length = 200)

class Customer(models.Model):
  id = models.AutoField(primary_key = True)
  person_id = models.ForeignKey(Person, on_delete=models.RESTRICT)
  is_active = models.BooleanField(default=False)
  is_deleted = models.BooleanField(default=False)

class Purchase(models.Model):
  id = models.AutoField(primary_key = True)
  customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
  iva = models.DecimalField(max_digits=5, decimal_places=2)
  subtotal = models.DecimalField(max_digits=5, decimal_places=2)
  total = models.DecimalField(max_digits=5, decimal_places=2)

class Category(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length = 200)
  description = models.TextField()

class Product(models.Model):
  id = models.AutoField(primary_key = True)
  category_id = models.ForeignKey(Category, on_delete=models.RESTRICT)
  name = models.CharField(max_length = 200)
  description = models.TextField()
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=5, decimal_places=2)

class PurchaseProducts(models.Model):
  id = models.AutoField(primary_key = True)
  product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)
  purchase_id = models.ForeignKey(Purchase, on_delete=models.RESTRICT)
  quantity = models.IntegerField()