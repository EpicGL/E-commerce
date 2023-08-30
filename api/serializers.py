from rest_framework import serializers
from cart.models import Order, OrderItem

class GetOrderserializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class getOrderItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'