from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

def info_view(request):
    products = Product.objects.all()
    context = {
        'app_name': 'E-Commerce App',
        'your_name': 'Will',
        'your_class': 'KKI',
        'products': products
    }
    return render(request, 'main1.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'addproduct.html', {'form': form})

def products_json(request):
    products = Product.objects.all()
    data = list(products.values('name', 'price', 'description', 'image'))
    return JsonResponse(data, safe=False)

def product_json_by_id(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        data = {
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'image': product.image.url if product.image else None  # Handle image URL
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        data = serializers.serialize("xml", [product])
        return HttpResponse(data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse('<error>Product not found</error>', content_type="application/xml")
