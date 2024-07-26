from django.contrib import admin
from django.urls import path, include

from app.views import StaticsPage

urlpatterns = [
    path('order_statistic/',StaticsPage.as_view(),name='order_price'),
    ]