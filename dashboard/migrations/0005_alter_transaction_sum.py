# Generated by Django 4.2.9 on 2024-07-11 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_transaction_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='sum',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999999)]),
        ),
    ]