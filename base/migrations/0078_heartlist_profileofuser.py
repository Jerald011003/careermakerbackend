# Generated by Django 4.1.7 on 2023-04-20 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0077_remove_heartlist_profileofuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartlist',
            name='profileofuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile'),
        ),
    ]
