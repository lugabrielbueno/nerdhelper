# Generated by Django 3.2.7 on 2021-09-30 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerds', '0009_nerd_nerdlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='nerd',
            name='nerdEmail',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
