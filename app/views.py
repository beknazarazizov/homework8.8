from django.db.models import Min, Max, Avg, Count
from django.shortcuts import render
from django.views import View

from app.models import Order, Product, Customer


# Create your views here.


class StaticsPage(View):
    def get(self, request):
        products = Product.objects.all()
        min_price_results = Product.objects.annotate(min_=Min("price"))
        min_price = (min_price_results.aggregate(min_price=Min("price"))['min_price']) // 20
        a_min_price = min_price * 20

        max_price_results = Product.objects.annotate(max_=Max("price"))
        max_price = (max_price_results.aggregate(max_price=Max("price"))['max_price']) // 20
        a_max_price = max_price * 20
        average_price_results = Product.objects.annotate(avg=Avg("price"))
        average_price = (average_price_results.aggregate(avg_price=Avg("price"))['avg_price']) // 20
        a_average_price = average_price * 20

        counting_result = Customer.objects.annotate(count=Count('id'))
        customers_count = counting_result.aggregate(count=Count('id'))['count']
        customers_count_st = customers_count * 10

        context = {'Products': products,
                   'min_price_st': min_price,
                   'min_price': a_min_price,
                   'max_price_st': max_price,
                   'max_price': a_max_price,
                   'average_price_st': average_price,
                   'average_price': a_average_price,
                   'customers_count': customers_count,
                   'customers_count_st': customers_count_st,
                   'temp': 20}
        return render(request, 'app/order_statistic.html', context)

