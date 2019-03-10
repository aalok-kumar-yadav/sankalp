from django.conf.urls import url
from social_media import  views
urlpatterns = [
    url(r'^$', views.social_media_news_feed, name='social_media_news_feed'),

]
