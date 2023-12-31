from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        product_counts = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_counts = products.count()

    context = {
        'products': products,
        'product_counts': product_counts,
    }

    return render(request, 'store/store.html', context)


