# Generated by Django 2.1.7 on 2019-02-24 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=400, unique=True)),
                ('event_name', models.CharField(max_length=300)),
                ('event_theme', models.CharField(max_length=300)),
                ('event_url', models.CharField(default=None, max_length=300)),
                ('event_place', models.CharField(default=None, max_length=3000)),
                ('event_timing', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.CharField(default=None, max_length=500)),
                ('profile_bio', models.CharField(default=None, max_length=1000)),
                ('registration_id', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('rating', models.FloatField(default=0.0)),
                ('ngo_slogan', models.CharField(max_length=200)),
                ('ngo_description', models.CharField(max_length=2000)),
                ('established_year', models.DateField(default=None)),
                ('website', models.CharField(max_length=300)),
                ('founded_by', models.CharField(max_length=200)),
                ('beneficiary_facility', models.CharField(max_length=700)),
                ('account_holder_name', models.CharField(default=None, max_length=100)),
                ('account_number', models.IntegerField(default=0)),
                ('IFSC_code', models.CharField(default=None, max_length=50)),
                ('branch_name', models.CharField(default=None, max_length=100)),
                ('verified', models.CharField(default='not verified', max_length=50)),
                ('city', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo_app.City')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.CharField(max_length=100, unique=True)),
                ('state_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ngo',
            name='state',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo_app.State'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='organized_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo_app.NGO'),
        ),
        migrations.AddField(
            model_name='city',
            name='city_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo_app.State'),
        ),
    ]
