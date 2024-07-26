from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()


    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    sold_date = models.DateField()



class Customer(models.Model):
    name= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    order_custom = models.ManyToManyField(Order, null=True, blank=True)

    def __str__(self):
        return self.name






# umumiy soni ,1 kunlik qilingan zakazlar narxi ,10 kunlik qilingan zakazlar soni



