from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Product
from .forms import ProductForm

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime
import json
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import Paginator # paginator bawaan django
from django.template.loader import render_to_string

@login_required(login_url='/login')
def show_main(request):
    context = {
        'app_name' : 'Garuda Gear',
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

def get_products_json(request):
    filter_type = request.GET.get("filter", "all")
    page_number = request.GET.get('page', 1)
    category_filter = request.GET.get('category', None)

    if filter_type == "all":
        product_objects = Product.objects.all().order_by('-pk')
    else:
        product_objects = Product.objects.filter(user=request.user).order_by('-pk')

    if category_filter:
        product_objects = product_objects.filter(category=category_filter)
        
    paginator = Paginator(product_objects, 9)  # 9 products per page
    page_obj = paginator.get_page(page_number)

    product_list = []
    for product in page_obj.object_list:
        product_list.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "brand": product.brand,
            "stock": product.stock,
            "description": product.description,
            "thumbnail": product.thumbnail,
            "category": product.get_category_display(),
            "is_featured": product.is_featured,
            "user_id": product.user.id
        })
    
    # render pagination HTML menjadi string
    pagination_html = render_to_string('pagination_links.html', {'products': page_obj, 'filter': filter_type})

    return JsonResponse({
        'products': product_list,
        'pagination_html': pagination_html,
    })

@csrf_exempt
@login_required(login_url='/login')
def add_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({"status": "success", "message": "Product added successfully!"}, status=201)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

@csrf_exempt
@login_required(login_url='/login')
def edit_product_ajax(request, id):
    try:
        product = Product.objects.get(pk=id, user=request.user)
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found or you don't have permission to edit it."}, status=404)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Product updated successfully!"})
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    
    if request.method == 'GET':
        product_data = {
            "name": product.name,
            "price": product.price,
            "brand": product.brand,
            "stock": product.stock,
            "description": product.description,
            "thumbnail": product.thumbnail,
            "category": product.category,
            "is_featured": product.is_featured,
        }
        return JsonResponse({"status": "success", "data": product_data})
        
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


@csrf_exempt
@login_required(login_url='/login')
def delete_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id, user=request.user)
            product.delete()
            return JsonResponse({"status": "success", "message": "Product deleted successfully!"})
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found or you don't have permission to delete it."}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Account created successfully!'}, status=201)
        else:
            errors = {field: error[0] for field, error in form.errors.items()}
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({'status': 'success', 'message': 'Login successful!'})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password.'}, status=401)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def logout_ajax(request):
    if request.method == 'POST':
        logout(request)
        response = JsonResponse({"status": "success", "message": "You have been logged out."})
        response.delete_cookie('last_login')
        return response
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

def add_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "add_product.html", context)

@login_required(login_url='/login')
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

def show_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        product_item = Product.objects.get(pk=id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# edit product
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

# hapus product
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# masuk about page
def about(request):
    context = {
        'app_name' : 'Garuda Gear',
        'username': request.user.username,
    }
    return render(request, "about.html", context)