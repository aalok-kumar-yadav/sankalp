"""
    Social media helper is helper function for providing
    all types of social media context data with json response

"""

from contributor_app.models import Contributor
from social_media.models import Post
from ngo_app.models import NGO
import random
from django.db.models import Q


# Function for getting timeline context data
def get_timeline_context(request, user_id):
    user_name = request.session['username']
    if user_name == user_id:
        gender_type = "You"
        con_status = "edit"
    else:
        gender_type = "him" if Contributor.objects.get(user__username=user_id) else "her"
        con_status = "connected"

    session_instance = Contributor.objects.get(user__username=user_id)
    user_post_list = Post.objects.filter(posted_by__user__username=user_id).order_by('-updated')
    timeline_context = {
        'username': user_name, 'user_info': {'first_name': request.session['first_name'],
                                           }, 'timeline_section': 'home',
        'con_status': con_status, 'user_activity': 'None',
        'user_data': session_instance, 'user_post_list': user_post_list}

    return timeline_context


# Function for getting timeline about context data
def get_timeline_about_context(request, user_id):
    user_name = request.session['username']
    if user_name == user_id:
        gender_type = "You"
        con_status = "edit"
    else:
        gender_type = "him" if Contributor.objects.get(user__username=user_id) else "her"
        con_status = "connected"

    contributor_instance = Contributor.objects.get(user__username=user_id)
    timeline_context = {

        'username': user_name, 'user_info': {'first_name': request.session['first_name'],
                                           }, 'gender_type': gender_type, 'timeline_section':
            'about', 'user_data': contributor_instance, 'con_status': con_status, 'user_activity': 'None'}

    return timeline_context


# Function for getting Latest News Feed
def get_news_feed(request):
    session_user = request.session['username']
    session_user_data = Contributor.objects.get(user__username=session_user)
    connected_people = Contributor.objects.filter(~Q(user__username=session_user))
    all_ngo_list = list(NGO.objects.all())
    random.shuffle(all_ngo_list)
    recommended_people_list = list(Contributor.objects.filter(~Q(user__username=session_user))) + all_ngo_list[:10]
    random.shuffle(recommended_people_list)
    user_post_list = Post.objects.all().order_by('-updated')
    context_data = {'username': session_user, 'user_info': {'first_name': request.session['first_name']},
                    'user_data': session_user_data, 'connected_people': connected_people[0:9],
                    'recommended_people': recommended_people_list[:6], 'page_type': 'news_feed',
                    'user_post_list': user_post_list}
    return context_data


# Helper function for getting Connected people
def get_connected_people(request, user_id):
    user_name = request.session['username']
    if user_name == user_id:
        con_status = "edit"
    else:
        con_status = "connected"

    connected_people = Contributor.objects.all()[:8]
    user_data = Contributor.objects.get(user__username=user_id)
    context_data = {'username': request.session['username'],
                    'user_info': {'first_name': request.session['first_name'], 'followers': '204',
                                  'gender_type': "him"}, 'timeline_section': 'connected_people', 'con_status': con_status,
                    'user_activity': [], 'connected_people': connected_people, 'user_data': user_data}

    return context_data


# Function for getting user/NGO Information
def get_session_user_info(request):
    user_instance = Contributor.objects.get(user__username=request.session['username'])
    context_data = {'username': request.session['username'],
                    'user_info': {'first_name': request.session['first_name'], 'followers': '204',
                                  'gender_type': "him"}, 'timeline_section': 'connected_people', 'con_status': "edit",
                    'user_activity': 'Aalok Kumar liked monisha wamankar post', 'user_info_edit': user_instance}
    return context_data
