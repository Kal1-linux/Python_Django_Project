from django.db import models


# Create your models here.
class Detail(models.Model):
    email = models.EmailField()
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

class Image(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to="media/")
    description = models.TextField(max_length=50)
    post = models.CharField(max_length=20)

class Userdata(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to="media/")
    description = models.TextField(max_length=50)
    post = models.CharField(max_length=20)

class Co(models.Model):
    pid = models.ForeignKey(Userdata,on_delete=models.CASCADE)
    nm = models.CharField(max_length=30)
    msg = models.CharField(max_length=100)

class Contacts(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Msg = models.CharField(max_length=100)