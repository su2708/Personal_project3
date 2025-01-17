# Generated by Django 4.2 on 2024-12-25 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0002_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="like_users",
            field=models.ManyToManyField(
                related_name="like_products", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
