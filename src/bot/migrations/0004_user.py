# Generated by Django 3.1.4 on 2021-01-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20210127_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('type_work', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
