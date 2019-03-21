"""
    Social media view is routing and rendering url based pages
    with user context data, this section have both Generic &
    Function based views.

"""

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View
from . import social_media_helpers as social_helper
from contributor_app.models import Contributor
from social_media.file_helper import *


# News Feed Generic View
class NewsFeed(View):
    def get(self, request):
        context_data = social_helper.get_news_feed(request)
        # import pdb;pdb.set_trace()
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


# Generic view for getting connected people
class ConnectedNgoPeople(View):

    def get(self, request, user_id):
        context_data = social_helper.get_connected_people(request, user_id)

        return render(request, 'timeline.html', context_data)

    def post(self, request):
        return render(request, 'timeline.html', {'timeline_section': 'connected_people'})


# Generic view for getting chat messaging page
class SocialMediaMessage(View):
    def get(self, request):
        return render(request, 'social_media_messages.html', {'username': request.session['username']})

    def post(self, request):
        return render(request, 'social_media_messages.html')


# Generic view for getting user/NGO timeline
class UserTimeline(View):
    def get(self, request, user_id):
        timeline_context = social_helper.get_timeline_context(request, user_id)
        return render(request, 'timeline.html', timeline_context)

    def post(self, request):
        return render(request, 'timeline.html', {'timeline_section': 'home'})


# Generic view for editing user/NGO profile
class EditProfile(View):
    def get(self, request):
        context_data = social_helper.get_session_user_info(request)
        return render(request, 'edit_profile.html', context_data)

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dob_date = request.POST.get("dob_date")
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        country = request.POST.get("country")
        user_name = request.session['username']
        profile_bio = request.POST.get("information")
        if request.FILES.get('profile_pic'):
            image_path = "/"+upload_profile_image(request)
        else:
            image_path = Contributor.objects.get(user__username=user_name).profile_image
        try:
            User.objects.filter(username=user_name).update(first_name=first_name, last_name=last_name)
            Contributor.objects.filter(user__username=user_name).update(dob=dob_date, gender="male", city=city, profile_image=image_path, country=country, profile_bio=profile_bio)
            request.session['first_name'] = first_name
        except Exception as e:
            print(e)
        context_data = social_helper.get_session_user_info(request)
        return render(request, 'edit_profile.html', context_data)


# Generic view for getting session user connected people
class TimelineConnection(View):
    def get(self, request):
        return render(request, 'timeline_connection.html')

    def post(self, request):
        return render(request, 'timeline_connection.html')


# Contact us page for contacting sankalp team
class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        return render(request, 'contact.html')


# Faq for getting Frequently asked question
class Faq(View):
    def get(self, request):
        return render(request, 'faq.html')

    def post(self, request):
        return render(request, 'faq.html')


# function view for standard custom 404 error
def error_404_view(request):
    return render(request, '404.html')


# Timeline About Generic View
class TimelineAbout(View):
    def get(self, request, user_id):
        context_data = social_helper.get_timeline_about_context(request, user_id)
        return render(request, 'timeline.html', context_data)

    def post(self, request):
        return render(request, 'timeline.html', {'timeline_section': 'about'})
