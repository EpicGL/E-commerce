from django.db import models
from product.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
                        ('pending', 'Pending'),
                        ('processing','Processing'),
                        ('completed','Completed'),
                        ('cancelled','Cancelled'),
                    ]
    customer = models.CharField(blank=True, max_length=264)
    complated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order_status = models.CharField( max_length=40, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        if self.updated != '':
            time = self.updated
        else: time = self.created
        return self.customer + "||" + str(time)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.getTotal for item in orderitems])
        return total 

class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        
    def __str__(self):
        return self.item.name + ' || '  + self.order.customer + ' || ' + str(self.created)
    
    @property
    def getTotal(self):
        return self.item.price * self.quantity
    
