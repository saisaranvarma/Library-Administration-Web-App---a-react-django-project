# Generated by Django 4.2.16 on 2024-11-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryadminapp', '0005_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='Image',
            field=models.ImageField(null=True, upload_to='users/'),
        ),
    ]