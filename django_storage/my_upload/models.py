from django.db import models
from datetime import datetime
import uuid
import django.utils


class Upload(models.Model):
    photo_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    upload_datetime = models.DateTimeField(default=django.utils.timezone.now)
    photo = models.ImageField(upload_to='photos/')