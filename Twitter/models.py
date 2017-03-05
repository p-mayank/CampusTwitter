from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class useradd(User):
    country = models.CharField(max_length = 100)
    profile_picture = models.FileField()

class useradmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'profile_picture']


class tweet(models.Model):
    text = models.CharField(max_length=1000)
    tweetto = models.ManyToManyField(useradd)
    tweetfrom = models.ForeignKey(useradd, related_name='+', on_delete=models.CASCADE, null=True)
    timestamp = models.TimeField(auto_now_add=True, blank=True)

class tweetadmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'tweetfrom', 'timestamp']

class comment(models.Model):
    ctext = models.CharField(max_length=1000)
    commenton = models.ForeignKey(tweet, on_delete=models.CASCADE)
    commentfrom = models.ForeignKey(useradd, on_delete=models.CASCADE, null=True)
    timestamp = models.TimeField(auto_now_add=True, blank=True)

