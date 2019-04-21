"""
    Social media view is routing and rendering url based pages
    with user context data, this section have both Generic &
    Function based views.

"""

from django.shortcuts import render
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View
from . import social_media_helpers as social_helper
from contributor_app.models import Contributor
from social_media.file_helper import *
import uuid
from social_media.models import Post, Event, UserPostLikeDislike, Comment
from social_media.file_helper import upload_file
from ngo_app.models import NGO
from django.http.response import JsonResponse


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
        session_user = request.session['username']
        session_user_data = Contributor.objects.get(user__username=session_user)
        connected_list = Contributor.objects.all()

        context_data = {'username': session_user, 'user_info': {'first_name': request.session['first_name']},
                        'user_data': session_user_data, 'connected_people': connected_list[1:10],
                        'nearby_people': connected_list[3:], 'recommended_people': connected_list[10:],
                        'page_type': 'nearby'}

        return render(request, 'news_feed.html', context_data)

    def post(self, request):
        people_list = Contributor.objects.all()[4:]
        context_data = {'people_list': people_list, 'page_type': 'nearby'}
        return render(request, 'news_feed.html', context_data)


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
            image_path = "/" + upload_file(request)
        else:
            image_path = Contributor.objects.get(user__username=user_name).profile_image
        try:
            User.objects.filter(username=user_name).update(first_name=first_name, last_name=last_name)
            Contributor.objects.filter(user__username=user_name).update(dob=dob_date, gender=gender, city=city,
                                                                        profile_image=image_path, country=country,
                                                                        profile_bio=profile_bio)
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
        return render(request, 'faq.html', {'user_info': {'first_name': request.session['first_name']},
                                            'username': request.session['username']})

    def post(self, request):
        return render(request, 'faq.html', {'user_info': {'first_name': request.session['first_name']},
                                            'username': request.session['username']})


# Timeline About Generic View
class TimelineAbout(View):
    def get(self, request, user_id):
        context_data = social_helper.get_timeline_about_context(request, user_id)
        return render(request, 'timeline.html', context_data)

    def post(self, request):
        return render(request, 'timeline.html', {'timeline_section': 'about'})


# simple view for creating post
def create_post(request):
    # import pdb;pdb.set_trace()

    post_desc = request.POST.get("post_description")
    post_id = uuid.uuid4().hex

    post_image = None
    post_video = None
    post_file = None
    # import pdb;pdb.set_trace()
    if request.FILES.get('add_post_image'):
        post_image = "/" + upload_file(request, 'post', 'add_post_image')
    if request.FILES.get('add_post_video'):
        post_video = "/" + upload_file(request, 'post', 'add_post_video')
    if request.FILES.get('add_post_file'):
        post_file = "/" + upload_file(request, 'post', 'add_post_file')

    posted_by = None
    if request.session['user_type'] == 'contributor':
        posted_by = Contributor.objects.get(user__username=request.session['username'])

    else:
        posted_by = NGO.objects.get(user__username=request.session['username'])

    try:
        # import pdb;pdb.set_trace()
        post_instance = Post(posted_by=posted_by, post_id=post_id, post_description=post_desc, post_image=post_image,
                             post_video=post_video, post_other_file=post_file)

        post_instance.save()
    except Exception as e:
        print(e)
    return redirect('news_feed')


# view for liking and dis liking user post
def like_dislike_post(request):

    username = request.session['username']
    post_id = dict(request.GET)['post_id'][0]
    rec_type = dict(request.GET)['rec_type'][0]
    post_ins = Post.objects.get(post_id=post_id)
    like_count = post_ins.like_count
    dislike_count = post_ins.dislike_count
    user_ins = User.objects.get(username=username)
    # import pdb;pdb.set_trace()

    reaction_ins = UserPostLikeDislike.objects.filter(post__post_id=post_id, user__username=username)

    # case when user first time like the new post
    if not reaction_ins and rec_type == 'like':
        print("first exc")
        try:
            like_count = like_count + 1
            Post.objects.filter(post_id=post_id).update(like_count=like_count)
            user_post_instance = UserPostLikeDislike(user=user_ins, post=post_ins, reaction_types=rec_type)
            user_post_instance.save()
        except Exception as e:
            print(e)
    # case when user first time dislikes the post
    elif not reaction_ins and rec_type == 'dislike':
        print("second exc")
        try:
            dislike_count = dislike_count + 1
            Post.objects.filter(post_id=post_id).update(dislike_count=dislike_count)
            user_post_instance = UserPostLikeDislike(user=user_ins, post=post_ins, reaction_types=rec_type)
            user_post_instance.save()
        except Exception as e:
            print(e)
    # case when user likes the already liked post
    elif reaction_ins and rec_type == 'like' and reaction_ins[0].reaction_types == 'like':
        print("third exc")
        try:
            like_count = like_count - 1
            Post.objects.filter(post_id=post_id).update(like_count=like_count)
            UserPostLikeDislike.objects.filter(post__post_id=post_id, user__username=username).update(
                reaction_types='default')
        except Exception as e:
            print(e)

        # case when user likes the already liked post
    elif reaction_ins and rec_type == 'like' and reaction_ins[0].reaction_types == 'default':
        print("fourth exc")
        try:
            like_count = like_count + 1
            Post.objects.filter(post_id=post_id).update(like_count=like_count)
            UserPostLikeDislike.objects.filter(post__post_id=post_id, user__username=username).update(
                reaction_types=rec_type)
        except Exception as e:
            print(e)

    # case when user likes the post already disliked
    elif reaction_ins and rec_type == 'like' and reaction_ins[0].reaction_types == 'dislike':
        print("fifth exc")
        try:
            like_count = like_count + 1
            dislike_count = dislike_count - 1
            Post.objects.filter(post_id=post_id).update(like_count=like_count, dislike_count=dislike_count)
            UserPostLikeDislike.objects.filter(post__post_id=post_id, user__username=username).update(reaction_types=rec_type)
        except Exception as e:
            print(e)

    # case when user dislikes the already dis liked post
    elif reaction_ins and rec_type == 'dislike' and reaction_ins[0].reaction_types == 'dislike':
        print("sixth exc")
        try:
            dislike_count = dislike_count - 1
            Post.objects.filter(post_id=post_id).update(dislike_count=dislike_count)
            UserPostLikeDislike.objects.filter(post__post_id=post_id, user__username=username).update(
                reaction_types='default')
        except Exception as e:
            print(e)

        # case when user dis likes the already dis liked post
    elif reaction_ins and rec_type == 'dislike' and reaction_ins[0].reaction_types == 'default':
        print("seventh exc")
        try:
            dislike_count = dislike_count + 1
            Post.objects.filter(post_id=post_id).update(dislike_count=dislike_count)
            UserPostLikeDislike.objects.filter(post__post_id=post_id, user__username=username).update(
                reaction_types=rec_type)
        except Exception as e:
            print(e)

    # case when user likes the post already disliked
    elif reaction_ins and rec_type == 'dislike' and reaction_ins[0].reaction_types == 'like':
        print("eighth exc")
        try:
            dislike_count = dislike_count + 1
            like_count = like_count - 1
            Post.objects.filter(post_id=post_id).update(like_count=like_count, dislike_count=dislike_count)
            UserPostLikeDislike.objects.filter(post__post_id=post_id, user__username=username).update(
                reaction_types=rec_type)
        except Exception as e:
            print(e)

    return JsonResponse({'post_id': post_id, 'like_count': like_count, 'dislike_count': dislike_count})


# view for sharing user post
def share_post():
    return {}


# view for commenting user post
def comment_post(request):

    username = request.session['username']
    post_id = dict(request.GET)['post_id'][0]
    comment = str(dict(request.GET)['comment'][0]).replace("%20", " ")
    post_ins = Post.objects.get(post_id=post_id)
    comment_ins = None
    comment_id = str(uuid.uuid4().hex)[:10]
    status = 'success'
    try:
        user_ins = Contributor.objects.get(user__username=username)
    except:
        user_ins = NGO.objects.get(user__username=username)
    try:
        comment_ins = Comment(comment_id=comment_id, post=post_ins, commented_user=user_ins, comment_desc=comment)
        comment_ins.save()
    except Exception as e:
        status = 'failure'
        print(e)

    return JsonResponse({'post_id': post_id, 'status': status, 'comment': comment, 'username': username})
