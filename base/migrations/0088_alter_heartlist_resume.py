# Generated by Django 4.1.7 on 2023-04-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0087_alter_heartlist_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartlist',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
