# Generated by Django 5.1 on 2024-09-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(max_length=255)),
                ('fruit_qty', models.IntegerField(max_length=11)),
                ('fruit_created', models.DateField()),
                ('fruit_updated', models.DateField()),
            ],
        ),
    ]
