from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path("account/", include("accounts.urls", namespace="accounts")),
    path('cart/', include('cart.urls', namespace='cart')),
    path("orders/", include("orders.urls", namespace="orders")),
    path("blog/", include("blog.urls", namespace="blog")),
    path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('', include('shop.urls', namespace='shop')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
