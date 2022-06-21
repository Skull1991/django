# Generated by Django 4.0.5 on 2022-06-19 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255)),
                ('item_price', models.FloatField()),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]