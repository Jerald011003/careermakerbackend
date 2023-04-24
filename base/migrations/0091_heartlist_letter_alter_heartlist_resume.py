# Generated by Django 4.1.7 on 2023-04-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0090_alter_heartlist_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartlist',
            name='letter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='heartlist',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
