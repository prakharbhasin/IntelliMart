# Generated by Django 3.2.3 on 2021-05-15 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_alter_store_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.owner'),
        ),
    ]