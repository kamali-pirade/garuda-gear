import uuid
from django.db import models

<<<<<<< HEAD
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('socks', 'Socks'),
        ('shoes', 'Shoes'),
        ('equipment', 'Equipment'),
        ('other', 'Other'),
=======
class News(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
>>>>>>> c41c600891abca760eaefccfc3f1c61fbed42336
    ]
    
    # Fitur wajib
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
<<<<<<< HEAD
    thumbnail = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
=======
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
>>>>>>> c41c600891abca760eaefccfc3f1c61fbed42336
    is_featured = models.BooleanField(default=False)

    # Fitur tambahan untuk Garuda Gear
    stock = models.IntegerField()
    brand = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
<<<<<<< HEAD
=======
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
>>>>>>> c41c600891abca760eaefccfc3f1c61fbed42336
