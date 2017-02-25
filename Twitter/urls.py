from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name= 'Twitter'

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^(?P<tweet_id>[0-9]+)/comment/$', views.commentadd, name='addcomment'),
]

