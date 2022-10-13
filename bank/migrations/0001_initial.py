# Generated by Django 4.1.2 on 2022-10-12 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Second_name', models.CharField(max_length=30)),
                ('First_name', models.CharField(max_length=30)),
                ('Third_name', models.CharField(max_length=30)),
                ('Passport', models.CharField(max_length=30)),
                ('Adress', models.CharField(max_length=60)),
                ('Salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CreditType',
            fields=[
                ('credit_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('credit_name', models.CharField(max_length=30)),
                ('interest_rate', models.IntegerField()),
                ('provision_condition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateField(verbose_name='submission date')),
                ('how_long', models.DateField(verbose_name='how long')),
                ('return_date', models.DateField(verbose_name='return date')),
                ('cost', models.IntegerField()),
                ('is_payed', models.BooleanField(default=False)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.client')),
                ('credit_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.credittype')),
            ],
        ),
    ]