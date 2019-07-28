from django.contrib.postgres.fields import JSONField
from django.db import models


class Category(models.Model):
    display_name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    image_url = models.CharField(max_length=256, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

