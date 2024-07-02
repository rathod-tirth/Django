from django.core.mail import send_mail
from django.conf import settings


def send_mails(val):
    subject = val.subject
    message = val.message
    from_email = settings.EMAIL_HOST_USER
    to_email = [val.to_email]
    # attachments=val.attachments
    status = send_mail(subject, message, from_email, to_email)
    if status:
        return True
    else:
        return False
