# Generated by Django 2.2.12 on 2020-04-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_auto_20200411_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=8)),
                ('u_password', models.CharField(max_length=16)),
            ],
        ),
    ]
