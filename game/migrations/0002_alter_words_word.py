# Generated by Django 5.0.7 on 2024-07-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='word',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
