# Generated by Django 3.2.7 on 2021-09-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerds', '0006_nerd_nerdsalt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nerd',
            name='nerdSalt',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
