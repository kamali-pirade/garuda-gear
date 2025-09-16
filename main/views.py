<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def show_main(request):
    products = Product.objects.all()

    context = {
        'app_name' : 'Garuda Gear',
        'name': 'Lessyarta Kamali Sopamena Pirade',
        'class': 'PBP C',
        'products': products
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "add_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, news_id):
    try:
        product_item = Product.objects.filter(pk=news_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, news_id):
    try:
        product_item = Product.objects.get(pk=news_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
=======
from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Garuda Gear',
        'name': 'Lessyarta Kamali Sopamena Pirade',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
>>>>>>> c41c600891abca760eaefccfc3f1c61fbed42336
