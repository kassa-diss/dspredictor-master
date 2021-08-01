
from django.db import models
from datetime import datetime
#importing django user default authenticaton
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.urls import reverse
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
    is_instuctor = models.BooleanField(default=False)


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
    resume = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_instuctor = models.BooleanField(default=True)


    def __str__(self):
        return self.user.username


class MyWorks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(max_length=1000,blank=True)
    picture_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    picture_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    picture_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    video = EmbedVideoField(blank=True)

class Event(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
