from .models import Product

def categories_processor(request):
    categories = Product.CATEGORY_CHOICES  # ambil pilihan kategori dari model Product
    return {'product_categories': categories}  # kembalikan dictionary dengan key 'product_categories'