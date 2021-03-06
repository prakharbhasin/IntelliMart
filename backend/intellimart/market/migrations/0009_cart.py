# Generated by Django 3.2.3 on 2021-05-20 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20210520_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='market.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.customer')),
            ],
        ),
    ]
