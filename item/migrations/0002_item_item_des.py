# Generated by Django 4.0.5 on 2022-06-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_des',
            field=models.TextField(blank=True),
        ),
    ]
