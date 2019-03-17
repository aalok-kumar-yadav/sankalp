from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View
from . import social_media_helpers as social_helper


# News Feed Generic View
class NewsFeed(View):
    def get(self, request, user_id):
        context_data = {}
        return render(request, 'news_feed.html', context_data)

    def post(self, request):
        context_data = {}
        return render(request, 'news_feed.html', context_data)


# NearByConnection Generic View
class NearByNgoPeople(View):

    def get(self, request):
        return render(request, 'nearby_ngo_people.html')

    def post(self, request):
        return render(request, 'nearby_ngo_people.html')


class ConnectedNgoPeople(View):

    def get(self, request):
        timeline_connected_context = {
            'user_info': {'first_name': request.session['first_name'],  'followers': '204', 'gender_type': 'him'},
            'timeline_section': 'connected_people', 'user_activity': 'Aalok Kumar liked monisha wamankar post'}

        return render(request, 'timeline.html', timeline_connected_context)

    def post(self, request):
        return render(request, 'timeline.html', {'timeline_section': 'connected_people'})


class SocialMediaMessage(View):
    def get(self, request):
        return render(request, 'social_media_messages.html')

    def post(self, request):
        return render(request, 'social_media_messages.html')


class UserTimeline(View):
    def get(self, request, user_id):
        timeline_context = social_helper.get_timeline_context(request, user_id)
        return render(request, 'timeline.html', timeline_context)

    def post(self, request):
        return render(request, 'timeline.html', {'timeline_section': 'home'})


class EditProfile(View):
    def get(self, request):
        return render(request, 'edit_profile.html')

    def post(self, request):
        return render(request, 'edit_profile.html')


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


# Timeline About Generic View
class TimelineAbout(View):
    def get(self, request, user_id):
        context_data = social_helper.get_timeline_about_context(request, user_id)
        return render(request, 'timeline.html', context_data)

    def post(self, request):
        return render(request, 'timeline.html', {'timeline_section': 'about'})
