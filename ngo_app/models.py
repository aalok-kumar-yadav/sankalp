from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    state_id = models.CharField(max_length=100, unique=True)
    state_name = models.CharField(max_length=100)


class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=500, default=None, null=True)
    profile_bio = models.CharField(max_length=1000, default=None, null=True)
    registration_id = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=200, default=None, null=True)
    state = models.OneToOneField(State, null=True, default=None, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, default=None, null=True)
    rating = models.FloatField(default=0.0,)
    funding_status = models.CharField(max_length=50, default=None)
    ngo_slogan = models.CharField(max_length=200, null=True)
    ngo_description = models.CharField(max_length=2000, default=None, null=True)
    established_year = models.DateField(default=None, null=True)
    website = models.CharField(max_length=300, null=True)
    founded_by = models.CharField(max_length=200, null=True)
    beneficiary_facility = models.CharField(max_length=700, null=True)
    account_holder_name = models.CharField(max_length=100, default=None, null=True)
    account_number = models.IntegerField(default=0, null=True)
    IFSC_code = models.CharField(max_length=50, default=None, null=True)
    branch_name = models.CharField(max_length=100, default=None, null=True)
    verified = models.CharField(max_length=50, default="not verified", null=True)

    def __str__(self):
        return "%s %s" % (self.user, self.city)


class Event(models.Model):
    event_id = models.CharField(unique=True, max_length=400)
    event_name = models.CharField(max_length=300)
    organized_by = models.ForeignKey(NGO, null=True, default=None, on_delete=models.CASCADE)
    event_theme = models.CharField(max_length=300)
    event_url = models.CharField(default=None, max_length=300)
    event_place = models.CharField(default=None, max_length=3000)
    event_timing = models.DateTimeField(default=None)

    def __str__(self):
        return self.event_id


