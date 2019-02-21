from django.conf.urls import url
from . import views

app_name = "shop"
urlpatterns = [

    url(r"^detail/(?P<id>[-\w]+)/(?P<slug>[-\w]+)/$",
        views.product_detail, name="product_detail"),
    url(r"^brand/(?P<brand_slug>[-\w]+)/$",
        views.product_list,
        name="product_list_by_brand"),
    url(r"^category/(?P<category_slug>[-\w]+)/$",
        views.product_list,
        name="product_list_by_category"),
    url(r"^$", views.base, name="base")
]
