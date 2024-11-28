# Generated by Django 4.2.16 on 2024-11-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryadminapp', '0003_users_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=250)),
                ('mail', models.EmailField(max_length=250, unique=True)),
                ('username', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('con_password', models.CharField(max_length=128)),
            ],
        ),
    ]
