# Generated by Django 3.2.7 on 2021-09-30 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerds', '0005_auto_20210927_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='nerd',
            name='nerdSalt',
            field=models.IntegerField(default=1),
        ),
    ]
