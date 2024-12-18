# Generated by Django 5.0.7 on 2024-09-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=10000)),
                ('author', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
