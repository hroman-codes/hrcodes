# Generated by Django 4.0.5 on 2024-01-05 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
