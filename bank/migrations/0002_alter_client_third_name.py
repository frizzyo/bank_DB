# Generated by Django 4.1.2 on 2022-10-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Third_name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
