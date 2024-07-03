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
        ("users/email_template_4th_of_July.html", "4th Of July"),
        ("users/email_template_father's_day.html", "Father's Day"),
        ("users/email_template_hotel_offer.html", "Hotel Offer"),
    )
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(
        widget=forms.Textarea, label="Message (fallback message):", required=False
    )
    username = forms.CharField(max_length=100, required=True)
    to_email = forms.EmailField(label="To", required=True)
    template = forms.ChoiceField(choices=choices, required=False)
    attachment = forms.FileField(required=False)
