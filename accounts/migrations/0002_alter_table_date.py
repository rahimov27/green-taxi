# Generated by Django 3.2.8 on 2021-11-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]