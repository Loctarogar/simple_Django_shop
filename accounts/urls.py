from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .import views

app_name = "accounts"

urlpatterns = [
    url(r"^logout$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^login$",
            auth_views.LoginView.as_view(template_name="accounts/login.html"),
            name="login"),
    url(r"^signup$", views.signup, name="signup"),
    url(r"^(?P<user_id>[-\w]+)$", views.account, name="account"),
]
