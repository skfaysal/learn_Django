# Generated by Django 3.1.7 on 2021-02-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField()),
                ('num2', models.IntegerField()),
            ],
        ),
    ]
