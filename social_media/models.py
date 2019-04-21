from django.db import models
from django.contrib.auth.models import User
from ngo_app.models import NGO
from contributor_app.models import Contributor


# Model class for account setting
class AccountSetting(models.Model):
    account = models.ForeignKey(User, null=False,  on_delete=models.CASCADE)
    can_receive_email = models.BooleanField(default=True, null=True)
    can_connect = models.BooleanField(default=True, null=True)
    send_me_notification = models.BooleanField(default=True, null=True)
    send_me_text_message = models.BooleanField(default=True, null=True)
    can_tag = models.BooleanField(default=True, null=True)
    enable_sound = models.BooleanField(default=True, null=True)

    def __str__(self):
        return "%s %s %s" % (self.account, self.enable_sound, self.can_connect)


# Model class for user/NGO post
class Post(models.Model):
    post_id = models.CharField(unique=True, null=False, max_length=500)
    posted_by = models.ForeignKey(Contributor or NGO, default=None, null=False,  on_delete=models.CASCADE)
    post_title = models.CharField(max_length=300, null=True)
    post_description = models.CharField(max_length=1000, null=True)
    post_image = models.ImageField(default=None, null=True)
    post_video = models.FileField(default=None, null=True)
    post_other_file = models.FileField(default=None, null=True)
    like_count = models.IntegerField(default=0, null=True)
    dislike_count = models.IntegerField(default=0, null=True)
    comment_count = models.IntegerField(default=0, null=True)
    share_count = models.IntegerField(default=0, null=True)
    is_sharable = models.BooleanField(default=True, null=True)
    visible = models.BooleanField(default=True, null=True)
    is_shared_post = models.CharField(max_length=100, default=None, null=True)
    original_posted_by = models.ForeignKey(User, default=None, null=True,  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.post_id, self.post_description, self.post_title)


#  Model class for NGO event
class Event(models.Model):
    event_id = models.CharField(max_length=500, unique=True, null=False)
    organized_by = models.ForeignKey(NGO, null=False, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=1000, null=False)
    event_description = models.CharField(max_length=2000, null=True)
    event_image = models.ImageField()
    event_theme = models.CharField(max_length=300, null=True, default=None)
    event_place = models.CharField(max_length=400, null=False)
    event_geo_location = models.CharField(max_length=200, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.event_id, self.event_description, self.organized_by)


# Model class for wanting volunteer
class Volunteer(models.Model):
    ngo = models.ForeignKey(NGO, null=False, on_delete=models.CASCADE)
    people_count = models.IntegerField(default=0)
    deadline = models.DateTimeField(default=None, null=True)
    description = models.CharField(max_length=500, default=None, null=True)
    current_status = models.IntegerField(default=0, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.ngo, self.people_count, self.description)


# Model class for User/NGO connected or not
class UserConnection(models.Model):
    first_user = models.ForeignKey(User, related_name='first_user', on_delete=models.CASCADE)
    second_user = models.ForeignKey(User, related_name='second_user', on_delete=models.CASCADE)
    relation_type = models.CharField(max_length=100, default="connection", null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.first_user, self.second_user)


class Comment(models.Model):
    comment_id = models.CharField(max_length=100, unique=True, null=False)
    comment_desc = models.CharField(max_length=1000, default=None, null=True)
    post = models.ForeignKey(Post, default=None, null=False,  on_delete=models.CASCADE)
    commented_user = models.ForeignKey(Contributor or NGO, default=None, null=False,  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.comment_id, self.comment_desc)


# Model class for Post Comment
class UserPostLikeDislike(models.Model):
    post = models.ForeignKey(Post, default=None, null=False,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, null=False,  on_delete=models.CASCADE)
    reaction_types = models.CharField(max_length=40, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.post, self.user)
