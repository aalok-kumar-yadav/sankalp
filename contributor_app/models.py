from django.db import models
from django.contrib.auth.models import User


# Model class for contributor
class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='/media/profile/default.jpg', null=True)
    profile_bio = models.CharField(max_length=1000, default=None, null=True)
    gender = models.CharField(max_length=50, null=True)
    dob = models.DateField(default=None, null=True)
    phone_number = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=100, null=True)
    contribution_domain = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.user, self.city)


# Model class for activity history
class ActivityHistory(models.Model):

    activity_type = models.CharField(max_length=200)
    reference_url = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


# Model class for contribution
class Contribution(models.Model):
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    contribution_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=300)
    contribution_type = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # ngo = models.ForeignKey(NGO, null=True, default=None)
    # transaction_id =


# Model class for transaction
class Transaction(models.Model):
    transaction_id = models.CharField(unique=True, max_length=1000)
    bank_transaction_id = models.CharField(max_length=1000)
    amount = models.IntegerField()
    user_id = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    beneficiary_ngo = models.CharField(max_length=200)
