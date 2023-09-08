from django.urls import path
from . import views
urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    path('product/', views.admin_product_m, name='productM'),
    path('inventory/', views.admin_inventory, name='inventory'),
    path('user-management/', views.admin_user_m, name='userM'),
    path('order-management', views.admin_order_m, name='orderM'),

]
