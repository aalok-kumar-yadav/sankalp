from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View


def social_media_news_feed(request):
    return render(request, 'social_media_news_feed.html', {'data': "hello kumar"})


class NearByNgoPeople(View):

    def get(self, request):
        return render(request, 'nearby_ngo_people.html')

    def post(self, request):
        return render(request, 'nearby_ngo_people.html')


class ConnectedNgoPeople(View):

    def get(self, request):
        return render(request, 'connected_ngo_people.html')

    def post(self, request):
        return render(request, 'connected_ngo_people.html')


class SocialMediaMessage(View):
    def get(self, request):
        return render(request, 'social_media_messages.html')

    def post(self, request):
        return render(request, 'social_media_messages.html')


class UserTimeline(View):
    def get(self, request):
        return render(request, 'user_timeline.html')

    def post(self, request):
        return render(request, 'user_timeline.html')


class EditProfile(View):
    def get(self, request):
        return render(request, 'edit_profile_basic.html')

    def post(self, request):
        return render(request, 'edit_profile_basic.html')


class TimelineConnection(View):
    def get(self, request):
        return render(request, 'timeline_connection.html')

    def post(self, request):
        return render(request, 'timeline_connection.html')


class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        return render(request, 'contact.html')


class Faq(View):
    def get(self, request):
        return render(request, 'faq.html')

    def post(self, request):
        return render(request, 'faq.html')


def error_404_view(request):
    return render(request, '404.html')
