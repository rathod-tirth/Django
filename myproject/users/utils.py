from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def send_mails(val):
    subject = val.subject
    message = val.message
    from_email = settings.EMAIL_HOST_USER
    to_email = val.to_email
    attachment = val.attachment
    mail = send_mail(subject, message, from_email, [to_email])
    # if status:
    #     return True
    # else:
    #     return False


def SendEmailMessage(subject, message, to_email, attachment):
    mail = EmailMessage(
        subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[to_email]
    )
    if attachment:
        mail.attach(attachment.name, attachment.read(), attachment.content_type)
    mail.send()
