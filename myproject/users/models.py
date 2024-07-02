from django.db import models

# Create your models here.


class SendEmail(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField()
    from_email = models.EmailField(max_length=254)
    to_email = models.EmailField(max_length=254)
    status = models.BooleanField()
    attachment = models.FileField(upload_to=None, max_length=100, blank=True)

    def __str__(self):
        return f"{self.to_email} | {self.subject}"
