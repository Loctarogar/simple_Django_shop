from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product, Brand
from cart.forms import CartAddProductForm
from .forms import PriceForm
from blog.forms import CommentForm
from blog.models import Comment


def base(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    featured_items = Product.objects.filter(features_items=True)
    recommended_item = Product.objects.filter(recommended_item=True)
    slider_items = Product.objects.filter(slider_item=True)

    cart_product_form = CartAddProductForm()

    return render(request, "shop/base.html",
                   {"brands": brands,
                    "categories": categories,
                    "featured_items": featured_items,
                    "recommended_item": recommended_item,
                    "cart_product_form": cart_product_form,
                    "slider_items": slider_items})


def product_list(request, category_slug=None, brand_slug=None):
    category = None
    brand = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    brands = Brand.objects.all()
    cart_product_form = CartAddProductForm()
    price_form = PriceForm(request.GET)

    featured_items = Product.objects.filter(features_items=True)
    recommended_item = Product.objects.filter(recommended_item=True)
    slider_items = Product.objects.filter(slider_item=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    elif brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)

    if price_form.is_valid():
        if price_form.cleaned_data["min_price"]:
            products = products.filter(price__gte=price_form.cleaned_data["min_price"])
        if price_form.cleaned_data["max_price"]:
            products = products.filter(price__lte=price_form.cleaned_data["max_price"])

    paginator = Paginator(products, 6)
    page = request.GET.get("page")

    products_list = paginator.get_page(page)
    return render(request, "shop/product_list.html",
                   {"category": category, "brand": brand,
                    "brands": brands, "price_form": price_form,
                    "categories": categories,
                    "products": products,
                    "featured_items": featured_items,
                    "slider_items": slider_items,
                    "recommended_item": recommended_item,
                    "cart_product_form": cart_product_form,
                    "products_list": products_list})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                slug=slug)
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    featured_items = Product.objects.filter(features_items=True)
    recommended_item = Product.objects.filter(recommended_item=True)
    slider_items = Product.objects.filter(slider_item=True)

    if product.product_comment:
        comments = product.product_comment.filter(active=True)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comment_author = request.user
            new_comment.product = product
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, "shop/detail.html",
                  {"product": product,
                   "brands": brands,
                   "categories": categories,
                   "cart_product_form": cart_product_form,
                   "featured_items": featured_items,
                   "slider_items": slider_items,
                   "recommended_item": recommended_item,
                   "comments": comments,
                   "comment_form": comment_form})

