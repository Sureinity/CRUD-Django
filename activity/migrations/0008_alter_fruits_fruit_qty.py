# Generated by Django 5.1 on 2024-09-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_alter_fruits_fruit_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruits',
            name='fruit_qty',
            field=models.IntegerField(blank=True),
        ),
    ]
