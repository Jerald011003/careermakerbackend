# Generated by Django 4.1.7 on 2023-04-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0081_alter_heartlist_canmessage_alter_heartlist_isheart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heartlist',
            old_name='description',
            new_name='userHeart',
        ),
        migrations.AddField(
            model_name='heartlist',
            name='userOwner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]