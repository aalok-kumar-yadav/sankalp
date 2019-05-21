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

from django.conf.urls import url, include
from django.contrib import admin
import social_media.urls as social_urls
from ngo_app import views
from django.conf import settings
from django.conf.urls.static import static
from contributor_app.views import about_us

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^social_media/', include(social_urls)),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'login/?', views.Login.as_view(), name ='diff_login'),
    url(r'accounts/login/', views.Login.as_view(), name='account_login'),
    url(r'^register', views.Register.as_view(), name='register'),
    url(r'^ngos$', views.all_ngo_view, name='all_ngo_view'),
    url(r'^search_ngo', views.SearchNgo.as_view(), name='search_ngo'),
    url(r'^ngos/description/(?P<ngo_id>.+)$', views.ngo_description, name='ngo_description'),
    url(r'^featured_ngo/(?P<category_name>.+)$', views.featured_ngo_category, name='featured_ngo'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^about_us', about_us, name='about_us'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)