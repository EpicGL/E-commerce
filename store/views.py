from django.shortcuts import render
from product.models import Product

def store(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'store.html',context)