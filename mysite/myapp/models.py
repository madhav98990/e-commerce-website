from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads')
    total_sales_amount = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)


def __str__(self):
        return self.name

from django.db import models
from myapp.models import Product  # adjust as per your app structure

class OrderDetail(models.Model):
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField()

    # Instamojo specific fields
    instamojo_payment_request_id = models.CharField(max_length=200, blank=True, null=True)
    instamojo_payment_id = models.CharField(max_length=200, blank=True, null=True)

    # Stripe specific field
    stripe_payment_intent = models.CharField(max_length=200, blank=True, null=True)

    has_paid = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_email} - {self.product.name} - ₹{self.amount}"
