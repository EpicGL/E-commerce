from django.shortcuts import render
from cart.models import Order, OrderItem
from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GetOrderserializers , getOrderItemsSerializers


@api_view(['GET'])
def get_order_id(request):
    try:
        order = Order.objects.filter(complated=False)
        if not order:
            raise Order.DoesNotExist
        serializer = GetOrderserializers(order, many=True)
        return Response(serializer.data[0])
    except Order.DoesNotExist: 
        return Response({"order":False})

@api_view(['GET'])
def get_Order_item(request , pk):
    order = Order.objects.get(pk=pk)
    orderitems = OrderItem.objects.filter(order=order)
    serializer = getOrderItemsSerializers(orderitems, many=True)
    return Response(serializer.data)

#add product to a cart or if the product is already on the cart then just incument the quantity
@api_view(['POST'])
def add_to_cart(request,pk):
    
    try:
        product = Product.objects.get(id=pk)

        order_id = request.data.get('order_id')
        
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
            except Order.DoesNotExist:
                order = Order.objects.create()
        else:
            order = Order.objects.create()
        
        existing_order_item = OrderItem.objects.filter(item=product , order=order).first()
        if existing_order_item:
            existing_order_item.quantity += 1
            existing_order_item.save()
            order_item = existing_order_item 
        else:
            order_item = OrderItem.objects.create(order=order, item=product)
        
        serializer = getOrderItemsSerializers(order_item)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"message": "Product not found."}, status=404)
    except Exception as e:
        return Response({"message": str(e)}, status=500)
    

@api_view(['POST'])
def decrement(request,pk):
    order_id = request.data.get('order_id')
    order = Order.objects.get(id=order_id)
    orderitem = OrderItem.objects.filter(item=Product.objects.get(id=pk) , order=order).first()
    if orderitem.quantity >1:
        orderitem.quantity -=1
        orderitem.save()
    else:
        return Response("Item quantity cant go below 1")
    return Response("Item quantity was decrement by 1")

@api_view(['DELETE'])
def removeItem(request,pk):
    order_id = request.data.get('order_id')
    order = Order.objects.get(id=order_id)
    orderitem = OrderItem.objects.filter(item=Product.objects.get(id=pk) , order=order).first()
    if orderitem:
        orderitem.delete()
        return Response("Item was removed")
    else:
        return Response("there is no item to remove")
    

@api_view(['GET'])
def total_cart(request,pk):
    try:
        order = Order.objects.get(id=pk)
        orderitem = OrderItem.objects.filter(order=order)
        total = 0
        if order.complated:
           return Response(total) 
        for i in orderitem:
            total += i.quantity
        
        return Response(total)
    except Exception as e:
        return Response({"no data"})