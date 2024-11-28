from django.db import models

class users(models.Model):
    Name = models.CharField(max_length=250)
    Age = models.IntegerField()
    Mail = models.EmailField(max_length=250, unique=True)
    Mobile = models.CharField(max_length=15, blank=True, null=True)
    Image = models.ImageField(upload_to='users/', null=True,blank=True)

class admin(models.Model):
    admin_name = models.CharField(max_length=250)
    mail = models.EmailField(max_length=250, unique=True)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=128)
    con_password = models.CharField(max_length=128)


class books(models.Model):
    bookname = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.CharField(max_length=3000)
    Image = models.ImageField(upload_to='users/', null=True,blank=True)