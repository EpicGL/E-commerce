from django.shortcuts import render ,redirect
from cart.models import Order, OrderItem


def cart(request, pk):
    order = Order.objects.get(id=pk)
    orderitems = OrderItem.objects.filter(order=order)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        if name != '':
            order.customer = str(name)
            order.complated = True
            order.save()
            return redirect('store')


    if len(orderitems) < 1:
        return redirect('store')
    
    total = sum(item.getTotal for item in orderitems)
    context = {'orderitems':orderitems, 'total': total}
    return render(request,'cart.html', context)

