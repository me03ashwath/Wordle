# Generated by Django 5.0.7 on 2024-07-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_length', models.IntegerField()),
                ('word', models.CharField(max_length=10)),
            ],
        ),
    ]
