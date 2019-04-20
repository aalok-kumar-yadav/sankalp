# Generated by Django 2.1.7 on 2019-03-25 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ngo_app', '0009_auto_20190325_1107'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_receive_email', models.BooleanField(default=True, null=True)),
                ('can_connect', models.BooleanField(default=True, null=True)),
                ('send_me_notification', models.BooleanField(default=True, null=True)),
                ('send_me_text_message', models.BooleanField(default=True, null=True)),
                ('can_tag', models.BooleanField(default=True, null=True)),
                ('enable_sound', models.BooleanField(default=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=500, unique=True)),
                ('event_name', models.CharField(max_length=1000)),
                ('event_description', models.CharField(max_length=2000, null=True)),
                ('event_image', models.ImageField(upload_to='')),
                ('event_theme', models.CharField(default=None, max_length=300, null=True)),
                ('event_place', models.CharField(max_length=400)),
                ('event_geo_location', models.CharField(default=None, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organized_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo_app.NGO')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500, unique=True)),
                ('post_title', models.CharField(max_length=300, null=True)),
                ('post_description', models.CharField(max_length=1000, null=True)),
                ('post_image', models.ImageField(default=None, null=True, upload_to='')),
                ('post_video', models.FileField(default=None, null=True, upload_to='')),
                ('post_other_file', models.FileField(default=None, null=True, upload_to='')),
                ('like_count', models.IntegerField(default=0, null=True)),
                ('dislike_count', models.IntegerField(default=0, null=True)),
                ('comment_count', models.IntegerField(default=0, null=True)),
                ('share_count', models.IntegerField(default=0, null=True)),
                ('is_sharable', models.BooleanField(default=True, null=True)),
                ('visible', models.BooleanField(default=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to=settings.AUTH_USER_MODEL)),
                ('second_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_count', models.IntegerField(default=0)),
                ('deadline', models.DateTimeField(default=None, null=True)),
                ('description', models.CharField(default=None, max_length=500, null=True)),
                ('current_status', models.IntegerField(default=0, null=True)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo_app.NGO')),
            ],
        ),
    ]
