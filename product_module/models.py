from django.db import models
from django.utils.html import mark_safe 
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=200)
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500) 
    price = models.FloatField()
    registered_on = models.DateTimeField()
    is_active = models.BooleanField()
    color_code = models.CharField(max_length=20)
    brand = models.ForeignKey (Brand, on_delete=models.CASCADE)
    category = models.ForeignKey (Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def image_tag(self): 
        return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />') 

    def __str__(self): 
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entered_on = models.DateTimeField()

class PaymentGateway(models.Model):
    token = models.UUIDField(default= uuid.uuid4,editable=False)
    expiry_date = models.DateField()
    balance = models.FloatField()
    is_active = models.BooleanField()