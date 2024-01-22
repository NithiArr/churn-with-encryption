# Generated by Django 4.1.2 on 2024-01-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerId', models.CharField(max_length=1000, null=True)),
                ('Surname', models.CharField(max_length=100)),
                ('CreditScore', models.IntegerField()),
                ('Geography', models.IntegerField()),
                ('Gender', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Tenure', models.IntegerField()),
                ('Balance', models.DecimalField(decimal_places=5, max_digits=50)),
                ('NumOfProducts', models.IntegerField()),
                ('HasCrCard', models.IntegerField()),
                ('IsActiveMember', models.IntegerField()),
                ('EstimatedSalary', models.DecimalField(decimal_places=5, max_digits=50)),
            ],
        ),
    ]