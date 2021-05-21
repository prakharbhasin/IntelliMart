# Generated by Django 3.2.3 on 2021-05-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_product_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='market/static/images/products'),
        ),
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(upload_to='market/static/images/logos'),
        ),
    ]