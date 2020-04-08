# Generated by Django 2.2.11 on 2020-04-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.IntegerField(unique=True)),
                ('u_name', models.CharField(max_length=16)),
                ('u_password', models.CharField(max_length=128)),
                ('u_icon', models.ImageField(upload_to='icons')),
            ],
        ),
    ]