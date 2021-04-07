
from django.db import models
from datetime import datetime
#importing django user default authenticaton
from django.contrib.auth.models import User
#extending to user profile

# class UserProfile(models.Model):
#     user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d/')
#     address = models.CharField(max_length=200,blank=True)
#     birth_date = models.DateField(default=datetime.now, blank=True)
#     bio = models.TextField(max_length=1000,blank=True)
#     email = models.EmailField(max_length=254, unique=True)
#     qualification = models.CharField(max_length=200,null=True)
#     guardian = models.CharField(max_length=150,null=True)
#     is_instuctor = models.BooleanField(default=False)
#     phone = models.CharField(max_length=12, unique=True)
#
#
#     def __str__(self):
#         return self.user.username

class Patient(models.Model):
    p_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d/')
    address = models.CharField(max_length=200,blank=True)
    birth_date = models.DateField(default=datetime.now, blank=True)
    bio = models.TextField(max_length=1000,blank=True)
    email = models.EmailField(max_length=254, unique=True)
    guardian = models.CharField(max_length=150,null=True)
    phone = models.CharField(max_length=12, unique=True)


    def __str__(self):
        return self.user.username

class Instructor(models.Model):
    in_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d/')
    address = models.CharField(max_length=200,blank=True)
    birth_date = models.DateField(default=datetime.now, blank=True)
    bio = models.TextField(max_length=1000,blank=True)
    email = models.EmailField(max_length=254, unique=True)
    qualification = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=12, unique=True)


    def __str__(self):
        return self.user.username
