# Generated by Django 4.1.7 on 2023-04-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0082_rename_description_heartlist_userheart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartlist',
            name='whotoheart',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]