# Generated by Django 2.1.7 on 2019-04-21 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contributor_app', '0001_initial'),
        ('social_media', '0002_auto_20190421_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.CharField(max_length=100, unique=True)),
                ('comment_desc', models.CharField(default=None, max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('commented_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contributor_app.Contributor')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='social_media.Post')),
            ],
        ),
    ]