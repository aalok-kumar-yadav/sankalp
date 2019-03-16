from django.db import models
from django.contrib.auth.models import User


class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=500, default=None, null=True)
    profile_bio = models.CharField(max_length=1000, default=None, null=True)
    gender = models.CharField(max_length=50, default=None)
    dob = models.DateField(default=None)
    phone_number = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=100)
    contribution_domain = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.user, self.city)


class Post(models.Model):
    post_id = models.CharField(unique=True, max_length=1000)
    post_title = models.CharField(max_length=300)
    post_description = models.CharField(max_length=1000)
    post_image_url = models.CharField(max_length=300)
    post_video_url = models.CharField(max_length=300)
    post_keyword = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.post_id


class ActivityHistory(models.Model):

    activity_type = models.CharField(max_length=200)
    reference_url = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class Contribution(models.Model):
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    contribution_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=300)
    contribution_type = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # ngo = models.ForeignKey(NGO, null=True, default=None)
    # transaction_id =


class Transaction(models.Model):
    transaction_id = models.CharField(unique=True, max_length=1000)
    bank_transaction_id = models.CharField(max_length=1000)
    amount = models.IntegerField()
    user_id = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    beneficiary_ngo = models.CharField(max_length=200)
