# Generated by Django 3.1.1 on 2020-09-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('airplane', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
            ],
        ),
    ]
