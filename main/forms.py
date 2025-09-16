from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",       
            "price",
            "brand", 
            "stock",
            "description",
            "thumbnail",  
            "category",
            "is_featured",
        ]