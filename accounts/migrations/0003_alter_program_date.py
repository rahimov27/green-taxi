# Generated by Django 3.2.8 on 2021-11-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_table_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]