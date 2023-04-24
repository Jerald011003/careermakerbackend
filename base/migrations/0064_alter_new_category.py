# Generated by Django 4.1.7 on 2023-04-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0063_new_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='category',
            field=models.CharField(blank=True, choices=[('sports', 'Sports'), ('gaming', 'Gaming'), ('politics', 'Politics')], max_length=50, null=True),
        ),
    ]