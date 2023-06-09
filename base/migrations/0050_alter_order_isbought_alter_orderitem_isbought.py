# Generated by Django 4.1.7 on 2023-04-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0049_alter_orderitem_isbought'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='isBought',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='isBought',
            field=models.BooleanField(default=True),
        ),
    ]
