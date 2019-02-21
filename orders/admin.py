from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    list_display = ["quantity", "get_cost"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', "user_id", 'first_name', 'last_name',
                    "get_total_cost", 'email', 'address', 'postal_code',
                    'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
