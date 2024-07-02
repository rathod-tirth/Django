from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("send-email/", send_email_view, name="send-email"),
    path(
        "send-email-with-template/",
        send_email_with_template_view,
        name="send-email-with-template",
    ),
    path("logout/", logout_view, name="logout"),
]
