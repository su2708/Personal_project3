from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.
def index(request):
    return render(request, "products/index.html")

def products(request):
    products = Product.objects.all().order_by("-id")
    context = {"products": products}
    return render(request, "products/products.html", context)

def product_detail(request, pk):
    pass

@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # 데이터가 바인딩된(값이 채워진) Form
        if form.is_valid():  # Form이 유효하다면 데이터를 저장하고 다른 곳으로 redirect
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect("products:product_detail", product.pk)
    # 기존 new 함수 부분
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/create.html", context)
