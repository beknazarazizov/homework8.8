from django.contrib import admin

from app.models import Product, Order, Customer

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
