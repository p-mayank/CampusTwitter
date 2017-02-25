from django.contrib import admin
from .models import useradd, tweet
from .models import useradmin, tweetadmin

# Register your models here.
admin.site.register(useradd, useradmin)
admin.site.register(tweet, tweetadmin)