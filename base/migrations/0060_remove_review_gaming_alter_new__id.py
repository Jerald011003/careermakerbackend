# Generated by Django 4.1.7 on 2023-04-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0059_sport_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='gaming',
        ),
        migrations.AlterField(
            model_name='new',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]