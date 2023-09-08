from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.models import Group


def store(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'store.html',context)