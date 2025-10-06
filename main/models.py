import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('socks', 'Socks'),
        ('shoes', 'Shoes'),
        ('equipment', 'Equipment'),
        ('other', 'Other'),
    ]
    
    # fitur wajib
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=0) # harga desimal agar bisa tampilan seperti 2,000,000
    description = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other') # default: other
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # fitur tambahan untuk Garuda Gear
    stock = models.IntegerField()
    brand = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
