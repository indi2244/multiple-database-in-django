# Generated by Django 4.2.15 on 2024-08-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wad', '0002_brand2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('founded', models.IntegerField()),
            ],
        ),
    ]
