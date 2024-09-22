import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required(login_url='/login')
def info_view(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'app_name': 'E-Commerce App',
        'your_name': 'Will',
        'your_class': 'KKI',
        'products': products,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, 'main1.html', context)

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Assign the logged-in user
            product.save()
            return redirect('main:info_view')  # Redirect to a success page or product list
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
            response = HttpResponseRedirect(reverse("main:info_view"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:info_view"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
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

