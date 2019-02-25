from django.contrib import admin
from contributor_app.models import Transaction, Contributor, Contribution, Post, ActivityHistory

admin.site.register(Transaction)
admin.site.register(Contribution)
admin.site.register(Contributor)
admin.site.register(Post)
admin.site.register(ActivityHistory)
