import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('socks', 'Socks'),
        ('shoes', 'Shoes'),
        ('equipment', 'Equipment'),
        ('other', 'Other'),
    ]
    
    # Fitur wajib
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)

    # Fitur tambahan untuk Garuda Gear
    stock = models.IntegerField()
    brand = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
