# Generated by Django 3.2.8 on 2021-11-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_remove_table_persons'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
        migrations.DeleteModel(
            name='Salad',
        ),
        migrations.DeleteModel(
            name='Specialty',
        ),
        migrations.DeleteModel(
            name='Starter',
        ),
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'client', 'verbose_name_plural': 'clients'},
        ),
        migrations.AddField(
            model_name='table',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
