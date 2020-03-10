from django.db import models
from django.conf import settings


class Attachment(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=settings.TRIX_URI)
    uploaded_at = models.DateTimeField(auto_now_add=True)
