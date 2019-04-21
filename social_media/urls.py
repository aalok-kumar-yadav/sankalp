from django.conf.urls import url
from social_media import views

urlpatterns = [
    url(r'^$', views.NewsFeed.as_view(), name='news_feed'),
    url(r'^nearby$', views.NearByNgoPeople.as_view(), name='nearby_ngo_people'),
    url(r'^connected/(?P<user_id>.+)$', views.ConnectedNgoPeople.as_view(), name='connected_ngo_people'),
    url(r'^messages$', views.SocialMediaMessage.as_view(), name='social_media_messages'),
    url(r'^timeline/(?P<user_id>.+)$', views.UserTimeline.as_view(), name='user_timeline'),
    url(r'^about/(?P<user_id>.+)$', views.TimelineAbout.as_view(), name='user_timeline_about'),
    url(r'^edit_profile$', views.EditProfile.as_view(), name='edit_profile'),
    url(r'^timeline_connection$', views.TimelineConnection.as_view(), name='timeline_connection'),
    url(r'^contact$', views.ContactUs.as_view(), name='contact_us'),
    url(r'^create_post', views.create_post, name='create_post'),
    url(r'^like_dislike_post', views.like_dislike_post, name='like_dislike_post'),
    url(r'^comment_post', views.comment_post, name='comment_post'),
    url(r'^faq$', views.Faq.as_view(), name='faq')
]
