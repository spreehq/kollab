# Generated by Django 2.1 on 2019-07-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20190728_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='hero_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
