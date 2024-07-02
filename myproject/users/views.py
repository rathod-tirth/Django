from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from .utils import send_mails


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")


def send_email_view(request):
    if request.method == "POST":
        form = forms.SendEmailForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            new_email = form.save(commit=False)
            status = send_mails(new_email)
            # print(new_email.subject)
            new_email.status = status
            new_email.save()
            form = forms.SendEmailForm()
    else:
        form = forms.SendEmailForm()
    return render(request, "users/send_email.html", {"form": form})
