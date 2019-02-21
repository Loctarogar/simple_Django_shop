from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from orders.models import OrderItem, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from shop.models import Category, Product, Brand


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def account(request, user_id):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    slider_items = Product.objects.filter(slider_item=True)
    user = get_object_or_404(User, pk=user_id)
    my_orders = Order.objects.filter(user=user)
    order_items = OrderItem.objects.all()
    return render(request, "accounts/my_acc.html",
                  {"brands": brands, "categories": categories,
                   "my_orders": my_orders, "order_items": order_items,
                   "slider_items": slider_items})
