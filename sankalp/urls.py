"""sankalp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from ngo_app import views
from contributor_app.views import EditContributorProfile

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^register', views.Register.as_view(), name='register'),
    url(r'^ngos', views.all_ngo_view, name='all_ngo_view'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^edit_user_profile$', EditContributorProfile.as_view(), name='edit_user_profile'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

]
