# Generated by Django 2.1.7 on 2019-04-18 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngo_app', '0019_auto_20190415_1132'),
        ('contributor_app', '0003_activityhistory_contribution_contributor_transaction'),
        ('social_media', '0003_auto_20190325_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posted_by',
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by_con',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contributor_app.Contributor'),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by_ngo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo_app.NGO'),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_user_image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
