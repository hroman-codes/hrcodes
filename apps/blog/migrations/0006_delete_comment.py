# Generated by Django 4.0.5 on 2024-01-05 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_like_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]