# Generated by Django 4.2.15 on 2024-08-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]