from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path("", posts_lists, name="list"),
    path("<slug:slug>", posts_page, name="page"),
]
