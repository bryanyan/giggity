# Generated by Django 3.0.4 on 2020-03-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('date_of_birth', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=11)),
                ('personal_info_displayed', models.BooleanField()),
                ('location', models.TextField(choices=[('San Francisco, CA', 'San Francisco, CA'), ('Other', 'Other')])),
                ('performer_category', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=10)),
                ('stage_name', models.CharField(blank=True, max_length=50)),
                ('facebook_link', models.URLField(blank=True)),
                ('youtube_link', models.URLField(blank=True)),
                ('soundcloud_link', models.URLField(blank=True)),
                ('spotify_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('website_link', models.URLField(blank=True)),
                ('profile_photo', models.FileField(blank=True, upload_to='')),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
