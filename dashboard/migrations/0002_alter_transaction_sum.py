# Generated by Django 4.2.9 on 2024-07-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='sum',
            field=models.IntegerField(),
        ),
    ]
