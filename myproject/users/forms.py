from django import forms
from .models import *

# Form With Model
# class SendEmailForm(forms.ModelForm):

#     class Meta:
#         model = SendEmail
#         fields = ["subject", "message", "to_email", "attachment"]


class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    to_email = forms.EmailField(label="To")
    attachment = forms.FileField(required=False)


class SendEmailWithTemplateForm(forms.Form):
    choices = (
        ("1", "template1"),
        ("2", "template2"),
        ("3", "template3"),
        ("4", "template4"),
    )
    subject = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    to_email = forms.EmailField(label="To", required=True)
    template = forms.ChoiceField(choices=choices, required=False)
    attachment = forms.FileField(required=False)
