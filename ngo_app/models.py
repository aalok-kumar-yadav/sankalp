from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    state_name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return "%s " % (self.state_name)


class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='/media/profile/default.jpg', null=True)
    cover_image = models.ImageField(default='/ngo/default.jpg', null=True)
    profile_bio = models.CharField(max_length=1000, default=None, null=True)
    registration_id = models.CharField(max_length=200)
    phone_number = models.CharField(default=None, max_length=30, null=True)
    address = models.CharField(max_length=1000, default=None, null=True)
    city = models.CharField(max_length=200, default=None, null=True)
    work_domain = models.CharField(max_length=400, default="Public Welfare", null=True)
    state = models.ForeignKey(State, null=True, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, default=None, null=True)
    rating = models.FloatField(default=0.0, null=True)
    funding_status = models.CharField(max_length=50, default=None, null=True)
    ngo_slogan = models.CharField(max_length=200, null=True)
    ngo_description = models.CharField(max_length=10000, default=None, null=True)
    established_year = models.DateField(default=None, null=True)
    website = models.CharField(max_length=300, null=True)
    founded_by = models.CharField(max_length=200, null=True)
    beneficiary_facility = models.CharField(max_length=700, null=True)
    account_holder_name = models.CharField(max_length=100, default=None, null=True)
    account_number = models.IntegerField(default=0, null=True)
    IFSC_code = models.CharField(max_length=50, default=None, null=True)
    branch_name = models.CharField(max_length=100, default=None, null=True)
    verified = models.CharField(max_length=50, default="not verified", null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s  %s" % (self.user, self.city)


