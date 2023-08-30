from django.urls import path
from . import views
urlpatterns = [
    path('orderid', views.get_order_id),
    path('orderitmes/<int:pk>', views.get_Order_item),
    path('add-to-cart/<int:pk>', views.add_to_cart),
    path('decrement/<int:pk>', views.decrement),
    path('remove-item/<int:pk>', views.removeItem),
    
    path('total-order-item/<int:pk>', views.total_cart),
]
