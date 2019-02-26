from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.views import View
from contributor_app.models import Contributor


class EditContributorProfile(View):

    def get(self, request):
        session_user = request.session['username']
        contrib_instance = Contributor.objects.get(user__username=session_user)
        return render(request, 'edit_contributor_profile.html', {'username': request.session['first_name'], 'profile': contrib_instance})

    def post(self, request):
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        profile_bio = request.POST.get('profile_bio')
        User.objects.filter(username=request.session['username']).update(first_name=first_name, email=email)
        Contributor.objects.filter(user__username=request.session['username']).update(phone_number=phone_number, profile_bio=profile_bio)
        request.session['first_name'] = first_name
        return redirect('profile')
