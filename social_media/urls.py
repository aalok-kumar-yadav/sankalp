from django.conf.urls import url
from social_media import views
from django.conf.urls import handler404

urlpatterns = [
    url(r'^$', views.social_media_news_feed, name='social_media_news_feed'),
    url(r'^nearby$', views.NearByNgoPeople.as_view(), name='nearby_ngo_people'),
    url(r'^connected$', views.ConnectedNgoPeople.as_view(), name='connected_ngo_people'),
    url(r'^messages$', views.SocialMediaMessage.as_view(), name='social_media_messages'),
    url(r'^timeline$', views.UserTimeline.as_view(), name='user_timeline'),
    url(r'^edit_profile$', views.EditProfile.as_view(), name='edit_profile'),
    url(r'^timeline_connection$', views.TimelineConnection.as_view(), name='timeline_connection'),
    url(r'^contact$', views.ContactUs.as_view(), name='contact_us'),
    url(r'^faq$', views.Faq.as_view(), name='faq')
]

handler404 = 'social_media.views.error_404_view'
