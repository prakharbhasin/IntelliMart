# Generated by Django 3.2.3 on 2021-05-21 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0011_auto_20210521_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.customer')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='quantities',
            field=models.ManyToManyField(to='market.CartQuantity'),
        ),
    ]
