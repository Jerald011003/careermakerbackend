# Generated by Django 4.1.7 on 2023-04-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_product_numofpreorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='watch',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]