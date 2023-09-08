from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Order, OrderItem
from product.models import Product, Category, Tag
from datetime import date, timedelta
import plotly.express as px 

@login_required
def admin_dashboard(request):
    today = date.today()
    order = Order.objects.filter(order_status = 'completed', created=today)

    print(order)

    nx = [c.created for c in order]
    ny = [ str(c.get_cart_total() for c in order)]
    nw = 0
    for sam in order:
        nw += sam.get_cart_total()

    fig = px.line(x = nx,
                  y = ny,
                  title=f'Total Sales Today: ${nw}',
                  labels={'x': 'Order Creation Date', 'y': 'Total Sales'},
                  )


    chart = fig.to_html()
    context = {'chart': chart}
    return render(request, 'admin_dashboard.html', context)

@login_required
def admin_product_m(request):
    return render(request, 'admin_new_product.html')

@login_required
def admin_inventory(request):
    return render(request, 'admin_inventory.html')


@login_required
def admin_order_m(request):
    pending_order = Order.objects.filter(order_status = 'pending').count
    processing_order = Order.objects.filter(order_status = 'processing').count
    completed_order = Order.objects.filter(order_status = 'completed').count
    cancelled_order = Order.objects.filter(order_status = 'cancelled').count
    
    order = Order.objects.get()

    context = {'pending_order':pending_order, 
               'processing_order': processing_order, 
               'completed_order':completed_order,
               'cancelled_order':cancelled_order,
               }
    return render(request, 'admin_order_management.html', context)


@login_required
def admin_user_m(request):
    return render(request, 'admin_user_management.html')
