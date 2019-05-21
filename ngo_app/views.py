from django.shortcuts import render
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View
from contributor_app.models import Contributor
from ngo_app.models import NGO, State
import random
from social_media import social_media_helpers as sm_helper
from django.contrib.auth import authenticate, login


# Index generic view for get & post request
class Index(View):

    def get(self, request):
        username = None
        first_name = None
        if 'username' in request.session:
            first_name = request.session['first_name']
            username = request.session['username']

        state_instance = State.objects.all()
        ngo_instance = NGO.objects.all()
        search_suggestion = []

        for item in state_instance:
            search_suggestion.append({'id': 1, 'name': item.state_name})
        for item in ngo_instance:
            search_suggestion.append({'id': 1, 'name': item.user.first_name})
        # import pdb;pdb.set_trace()
        return render(request, 'index.html',
                      {'first_name': first_name, 'username': username, 'search_suggestion': search_suggestion})

    def post(self, request):
        username = None
        first_name = None
        if 'username' in request.session:
            first_name = request.session['first_name']
            username = request.session['username']
        return render(request, 'index.html', {'first_name': first_name, 'username': username})


# Logout view for flushing the session
def logout(request):
    request.session.flush()
    return redirect('index')


# Login generic view for user/NGO login
class Login(View):
    def get(self, request):
        full_path = request.get_full_path()
        next = ""
        if 'next' in full_path:
            next = request.GET['next']
        return render(request, 'register_login.html', {'message': 'valid', 'type': 'login', 'next': next})

    def post(self, request):
        user_name = request.POST.get("email")
        password = request.POST.get("password")
        auth_user = authenticate(username=str(user_name).split('@')[0], password=password)
        if auth_user:
            request.session['username'] = str(user_name).split('@')[0]
            request.session['first_name'] = auth_user.first_name
            try:
                NGO.objects.get(user__username=user_name)
                request.session['user_type'] = 'ngo'
            except:
                request.session['user_type'] = 'contributor'
            login(request, auth_user)
            next = ""
            full_path = request.get_full_path()
            if 'next' in full_path:
                next = request.GET['next']
            # import pdb;pdb.set_trace()
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('index')
        else:
            return render(request, 'register_login.html', {'message': 'invalid', 'type': 'login'})


# Register generic view for registering User/NGO
class Register(View):
    def get(self, request):
        return render(request, 'register_login.html', {'message': "valid", 'type': 'register'})

    def post(self, request):
        user_type = request.POST.get("user_type")

        try:
            if user_type == 'contributor':  # If condition for contributor registration
                dob = request.POST.get("dob_date")
                email = request.POST.get("user_email")
                user_password = request.POST.get("user_password")
                gender = request.POST.get("gender")
                city = request.POST.get("user_city")
                country = request.POST.get("user_country")
                user_instance = User.objects.create_user(str(email).split('@')[0], email, user_password)
                user_instance.first_name = request.POST.get("first_name")
                user_instance.last_name = request.POST.get('last_name')
                user_instance.save()
                contributor = Contributor(user=user_instance, dob=dob, gender=gender, city=city, country=country)
                contributor.save()
                return redirect('index')
            else:  # Else condition for registering ngo profile
                yof = request.POST.get("yof_date")
                email = request.POST.get("ngo_email")
                ngo_password = request.POST.get("ngo_password")
                funding_status = request.POST.get("funding_status")
                city = request.POST.get("ngo_city")
                country = request.POST.get("ngo_country")
                user_instance = User.objects.create_user(str(email).split('@')[0], email, ngo_password)
                user_instance.first_name = request.POST.get("ngo_name")
                user_instance.save()
                ngo_instance = NGO(user=user_instance, established_year=yof, funding_status=funding_status, city=city,
                                   country=country)
                ngo_instance.save()
                return redirect('index')
        except IntegrityError:
            return render(request, 'register_login.html', {'message': 'invalid', 'type': 'register'})


# All ngo view for getting all NGO
def all_ngo_view(request):
    first_name, username = sm_helper.get_request_user_info(request)
    ngo_queryset = list(NGO.objects.all())
    random.shuffle(ngo_queryset)
    return render(request, 'all_ngo.html',
                  {'first_name': first_name, 'username': username, 'ngo_list': ngo_queryset})


# Function based view for featured ngo category
def featured_ngo_category(request, category_name):
    first_name, username = sm_helper.get_request_user_info(request)
    featured_ngo_list = NGO.objects.filter(work_domain__contains=category_name)
    return render(request, 'ngo_search.html',
                  {'first_name': first_name, 'username':username,
                   'ngo_display': 'featured', 'search_keyword': category_name, 'ngo_search_result': featured_ngo_list})


# Ngo description view
def ngo_description(request, ngo_id):
    first_name, username = sm_helper.get_request_user_info(request)
    ngo_instance = NGO.objects.get(user__username=ngo_id)
    return render(request, 'ngo_description.html',
                  {'first_name': first_name, 'username': username, 'ngo_info': ngo_instance})


# function view for standard custom 404 error
def handler404(request):
    return render(request, '404.html')


# Class based view for searching user query about ngo
class SearchNgo(View):

    def get(self, request):
        first_name = None
        try:
            first_name = request.session['first_name']
        except Exception as e:
            print(e)
        return render(request, 'ngo_search',
                      {'first_name': first_name, 'username': request.session['username'], 'ngo_display': 'ngo_search'})

    def post(self, request):
        # import pdb;pdb.set_trace()
        first_name = None
        try:
            first_name = request.session['first_name']
        except Exception as e:
            print(e)
        search_keyword = request.POST.get("search_ngo")
        search_filter_list = State.objects.filter(state_name=search_keyword)
        if not search_filter_list:
            search_filter_list = NGO.objects.filter(user__first_name__contains=search_keyword)
        else:
            search_filter_list = NGO.objects.filter(state__state_name__contains=search_keyword)
        state_instance = State.objects.all()
        ngo_instance = NGO.objects.all()
        search_suggestion = []

        for item in state_instance:
            search_suggestion.append({'id': 1, 'name': item.state_name})
        for item in ngo_instance:
            search_suggestion.append({'id': 1, 'name': item.user.first_name})

        return render(request, 'ngo_search.html', {'first_name': first_name, 'username': request.session['username'],
                                                   'search_keyword': search_keyword,
                                                   'ngo_search_result': search_filter_list,
                                                   'search_suggestion': search_suggestion, 'ngo_display': 'ngo_search'})
