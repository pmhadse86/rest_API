from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()
        city = models.CharField(max_length=100)
        marks = models.IntegerField()
        is_deleted = models.SmallIntegerField(default= 0)
        
        ## for DRF filtering..
        created_by = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

        def __str__(self):
                return self.name

        class Meta:
                db_table = 'stud'

class College(models.Model):
        name = models.CharField(max_length=100)
        staff_count = models.IntegerField()

        def __str__(self):
                return self.name
        
        class Meta:
                db_table = 'colg'


###   signal generation after user creation to create

from django.conf import settings 
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender = User)         ##AUTH_USER_MODEL     ##  settings.AUTH_USER_MODEL
def create_auth_token(sender, instance= None, created= False, **kwargs):
        if created:
                Token.objects.create(user= instance)


@receiver(post_save, sender = Student)
def say_hello(sender, instance, created, **kwargs):
        if created:
                print(f" Hi your profile is created {instance.name}")

@receiver(pre_save, sender = Student)
def say_hello(sender, instance, created= None, **kwargs):
        # if created:
                print(f" Hi your profile is about to create {instance.name}")

@receiver(post_delete, sender = Student)
def say_bye(sender, instance, created= None, **kwargs):
        # if created:
                print(f" Hi your profile is deleted {instance.name}")



#####   Serializer relations
class Album(models.Model):
        album_name = models.CharField(max_length=100)
        artist = models.CharField(max_length=100)

        def __str__(self):
                return self.album_name
        class Meta:
                db_table = 'album'

class Track(models.Model):
        order = models.IntegerField()
        title = models.CharField(max_length= 100)
        duration = models.IntegerField()
        album = models.ForeignKey(Album, related_name='tracks', on_delete= models.CASCADE)
        
        class Meta:
                unique_together = ['album', 'order']
                ordering = ['order']
        def __str__(self):
                return f" {self.order}  ----  {self.title}"