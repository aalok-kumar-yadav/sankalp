# Generated by Django 2.1.7 on 2019-04-20 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0006_auto_20190420_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contributor_app.Contributor'),
        ),
    ]
