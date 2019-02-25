from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    state_id = models.CharField(max_length=100, unique=True)
    state_name = models.CharField(max_length=100)


class City(models.Model):
    city_id = models.CharField(max_length=100, unique=True)
    city_name = models.ForeignKey(State, on_delete=models.CASCADE)


class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=500, default=None)
    profile_bio = models.CharField(max_length=1000, default=None)
    registration_id = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    city = models.ForeignKey(City, null=True, default=None, on_delete=models.CASCADE)
    state = models.OneToOneField(State, null=True, default=None, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    ngo_slogan = models.CharField(max_length=200)
    ngo_description = models.CharField(max_length=2000)
    established_year = models.DateField(default=None)
    website = models.CharField(max_length=300)
    founded_by = models.CharField(max_length=200)
    beneficiary_facility = models.CharField(max_length=700)
    account_holder_name = models.CharField(max_length=100, default=None)
    account_number = models.IntegerField(default=0)
    IFSC_code = models.CharField(max_length=50, default=None)
    branch_name = models.CharField(max_length=100, default=None)
    verified = models.CharField(max_length=50, default="not verified")


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


