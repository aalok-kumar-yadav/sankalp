from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View
from contributor_app.models import Contributor
from ngo_app.models import NGO


# Index generic view for get & post request
class Index(View):

    def get(self, request):
        username = None
        first_name = None
        if 'username' in request.session:
            first_name = request.session['first_name']
            username = request.session['username']
        return render(request, 'index.html', {'first_name': first_name, 'username': username})

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
        return render(request, 'register_login.html', {'message': 'valid', 'type': 'login'})

    def post(self, request):
        user_name = request.POST.get("email")
        password = request.POST.get("password")
        auth_user = authenticate(username=str(user_name).split('@')[0], password=password)

        if auth_user:
            request.session['username'] = str(user_name).split('@')[0]
            request.session['first_name'] = auth_user.first_name
            return redirect('index')
        else:
            return render(request, 'register_login.html', {'message': 'invalid', 'type': 'login'})


# Register generic view for registering User/NGO
class Register(View):
    def get(self, request):
        return render(request, 'register_login.html', {'message': "valid", 'type': 'login'})

    def post(self, request):
        user_type = request.POST.get("user_type")

        try:
            if user_type == 'contributor':
                dob = request.POST.get("dob_date")
                email = request.POST.get("user_email")
                user_password = request.POST.get("user_password")
                gender = "male" if request.POST.get("male") else "female"
                city = request.POST.get("user_city")
                country = request.POST.get("user_country")
                user_instance = User.objects.create_user(str(email).split('@')[0], email, user_password)
                user_instance.first_name = request.POST.get("first_name")
                user_instance.last_name = request.POST.get('last_name')
                user_instance.save()
                contributor = Contributor(user=user_instance, dob=dob, gender=gender, city=city, country=country)
                contributor.save()
                return redirect('index')
            else:
                yof = request.POST.get("yof_date")
                email = request.POST.get("ngo_email")
                ngo_password = request.POST.get("ngo_password")
                funding_status = "Funded" if request.POST.get("funded") else "Not funded"
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
    first_name = None
    try:
        first_name = request.session['first_name']
    except Exception as e:
        print(e)

    return render(request, 'all_ngo.html', {'username': first_name})

