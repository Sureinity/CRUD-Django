# Generated by Django 5.1 on 2024-09-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_alter_fruits_fruit_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruits',
            name='fruit_qty',
            field=models.IntegerField(),
        ),
    ]
