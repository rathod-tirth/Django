from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string


# send mail without attachment
def send_mails(val):
    status = send_mail(
        subject=val.subject,
        message=val.message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[val.to_email],
    )
    if status:
        return True
    else:
        return False


# send mail with attachment
def SendEmailMessage(subject, message, to_email, attachment):
    mail = EmailMessage(
        subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[to_email]
    )
    if attachment:
        mail.attach(attachment.name, attachment.read(), attachment.content_type)
    mail.send()


# sending email with html template
def SendEmailWithTemplate(subject, message, username, to_email, template, attachment):
    mail = EmailMultiAlternatives(
        subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[to_email]
    )

    # rendering template
    html_template = render_to_string(template, {"username": username})
    mail.attach_alternative(html_template, "text/html")

    if attachment:
        mail.attach(attachment.name, attachment.read(), attachment.content_type)
    mail.send()
