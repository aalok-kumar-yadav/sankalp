from django.contrib import admin
from social_media.models import AccountSetting, Post, Event, Volunteer, UserConnection, UserPostLikeDislike, Comment


admin.site.register(AccountSetting)
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Volunteer)
admin.site.register(UserConnection)
admin.site.register(UserPostLikeDislike)
admin.site.register(Comment)
