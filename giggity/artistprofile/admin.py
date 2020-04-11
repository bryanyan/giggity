from django.contrib import admin

from .models import ArtistProfile

class ArtistProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		('Required', {'fields': ['full_name', 'email', 'password', 'date_of_birth', 'phone_number', 'personal_info_displayed', 'location', 'performer_category', 'genre']}),
		('Optional', {'fields': ['stage_name', 'facebook_link', 'youtube_link', 'soundcloud_link', 'spotify_link', 'instagram_link', 'website_link', 'profile_photo', 'bio']})
	]
	list_display = ('full_name', 'email', 'performer_category', 'genre')
	list_filter = ['performer_category', 'genre']
	search_fields = ['full_name']

admin.site.register(ArtistProfile, ArtistProfileAdmin)