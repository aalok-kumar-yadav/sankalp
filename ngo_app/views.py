from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View
from contributor_app.models import Contributor


class Index(View):
    def get(self, request):
        username = None
        if 'username' in request.session:
            username = request.session['first_name']
        return render(request, 'index.html', {'username': username})

    def post(self, request):
        # Code block for POST request
        return


def logout(request):
    request.session.flush()
    return redirect('index')


class Login(View):
    def get(self, request):
        return render(request, 'login.html', {'message': 'valid', 'type': 'login'})

    def post(self, request):
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        auth_user = authenticate(username=user_name, password=password)
        if auth_user:
            request.session['username'] = user_name
            request.session['first_name'] = auth_user.first_name
            return redirect('index')
        else:
            return render(request, 'login.html', {'message': 'invalid', 'type': 'login'})


class Register(View):
    def get(self, request):
        return render(request, 'login.html', {'message': 'valid', 'type': 'register'})

    def post(self, request):
        try:
            user_instance = User.objects.create_user(request.POST.get('username'), request.POST.get('email'),
                                                     request.POST.get('password'))
            user_instance.first_name = request.POST.get('first_name')
            user_instance.last_name = request.POST.get('last_name')
            user_instance.save()
            return redirect('index')

        except IntegrityError:
            return render(request, 'login.html', {'message': 'invalid', 'type': 'register'})


def all_ngo_view(request):

    return render(request, 'all_ngo.html', {'data': "alok"})


def profile(request):
    contributor_instance = Contributor.objects.get(user__username=request.session['username'])
    return render(request, 'profile.html', {'profile': contributor_instance})
