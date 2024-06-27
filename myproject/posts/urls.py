from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path("", posts_lists, name="list"),
    path("new-post", post_new, name="new-post"),
    path("<slug:slug>", post_page, name="page"),
]
