from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from .utils import send_mails, SendEmailMessage, SendEmailWithTemplate


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
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            to_email = form.cleaned_data["to_email"]
            attachment = request.FILES.get("attachment")

            SendEmailMessage(subject, message, to_email, attachment)

            form = forms.SendEmailForm()
    else:
        form = forms.SendEmailForm()
    return render(request, "users/send_email.html", {"form": form})


def send_email_with_template_view(request):
    if request.method == "POST":
        form = forms.SendEmailWithTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            username = form.cleaned_data["username"]
            to_email = form.cleaned_data["to_email"]
            template = form.cleaned_data["template"]
            attachment = request.FILES.get("attachment")

            SendEmailWithTemplate(
                subject, message, username, to_email, template, attachment
            )

            form = forms.SendEmailWithTemplateForm()

    else:
        form = forms.SendEmailWithTemplateForm()
    return render(request, "users/send_email_with_template.html", {"form": form})
