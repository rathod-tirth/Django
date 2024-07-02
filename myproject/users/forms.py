from django import forms
from .models import *


class SendEmailForm(forms.ModelForm):

    class Meta:
        model = SendEmail
        fields = ["subject", "message", "to_email", "attachment"]
