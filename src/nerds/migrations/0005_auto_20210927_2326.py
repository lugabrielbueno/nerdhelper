# Generated by Django 3.2.7 on 2021-09-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerds', '0004_nerd_nerdfowards'),
    ]

    operations = [
        migrations.AddField(
            model_name='nerd',
            name='nerdLogin',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AddField(
            model_name='nerd',
            name='nerdPassword',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
