# Generated by Django 4.1.7 on 2023-04-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0085_rename_isheart_profile_isverified'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartlist',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
