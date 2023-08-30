from django.shortcuts import render
from .models import Product
def viewProduct(request,slug):
    product = Product.objects.get(slug=slug)
    context = {"product": product}
    return render(request,'product.html',context)