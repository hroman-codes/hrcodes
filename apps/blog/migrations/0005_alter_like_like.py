# Generated by Django 4.0.5 on 2024-01-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_likes_like_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
