from typing import Iterable, Optional
from django.db import models
from autoslug import AutoSlugField


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name',unique=True, blank=False)
    def __str__(self):
        return self.name

# Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/',default='product_images/default_product_image.jpg')
    slug = AutoSlugField(populate_from='name', unique=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='default')
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def slugURL(self):
        url =  'product/'+self.slug
        return str(url)