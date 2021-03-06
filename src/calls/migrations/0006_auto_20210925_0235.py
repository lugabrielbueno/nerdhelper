# Generated by Django 3.2.7 on 2021-09-25 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0005_call_solution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='call',
            old_name='solution',
            new_name='solutionCall',
        ),
        migrations.RenameField(
            model_name='call',
            old_name='status',
            new_name='statusCall',
        ),
        migrations.AddField(
            model_name='call',
            name='nerdCall',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='call',
            name='clientCall',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='call',
            name='companyCall',
            field=models.CharField(max_length=30),
        ),
    ]
