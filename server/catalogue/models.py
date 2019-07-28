from django.contrib.postgres.fields import JSONField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Brand(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.CharField(max_length=256)
    logo_url = models.CharField(max_length=512)
    single_liner = models.CharField(max_length=256)
    cta_text = models.CharField(max_length=256)
    hero_url = models.CharField(max_length=512, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class BrandAssociations(models.Model):
    source = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='source')
    destination = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='destination')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('source__name', 'destination__name', )

    def __str__(self):
        return f'{self.source.name} -> {self.destination.name}'
