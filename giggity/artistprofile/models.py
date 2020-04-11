from django.db import models
from django.urls import reverse
from datetime import datetime


class ArtistProfile(models.Model):
	#required fields
	full_name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=50)
	date_of_birth = models.DateTimeField()
	phone_number = models.CharField(max_length=11)
	personal_info_displayed = models.BooleanField()


	LOCATIONS = (
		('San Francisco, CA', 'San Francisco, CA'),
		('Other', 'Other'),
	)
	location = models.TextField(choices=LOCATIONS)

	PerformerType = models.TextChoices('PerformerType', 'DJ SINGER BAND OTHER')
	performer_category = models.CharField(choices=PerformerType.choices, max_length=10)

	GenreType = models.TextChoices('GenreType', 'EDM R&B HIP-HOP LATIN OTHER')
	genre = models.CharField(choices=GenreType.choices, max_length=10)

	profile_creation_date = models.DateTimeField(default=datetime.now, editable=False)



	#optional fields
	stage_name = models.CharField(blank=True, max_length=50)
	facebook_link = models.URLField(blank=True)
	youtube_link = models.URLField(blank=True)
	soundcloud_link = models.URLField(blank=True)
	spotify_link = models.URLField(blank=True)
	instagram_link = models.URLField(blank=True)
	website_link = models.URLField(blank=True)
	profile_photo = models.FileField(blank=True)
	bio = models.TextField(blank=True)

	def __str__(self):
		return self.full_name

	def get_absolute_url(self):
		return reverse('artistprofile:detail', args=[self.id])

	

