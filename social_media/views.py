from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View


def social_media_news_feed(request):

    return render(request, 'social_media_news_feed.html', {'data': "hello kumar"})