# Generated by Django 5.1.4 on 2024-12-10 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('carbs', models.FloatField()),
                ('proteins', models.FloatField()),
                ('fats', models.FloatField()),
                ('calories', models.PositiveBigIntegerField()),
            ],
        ),
    ]
