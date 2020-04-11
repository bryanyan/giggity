from django.views import generic

from .models import ArtistProfile


class IndexView(generic.ListView):
	template_name = 'artistprofile/index.html'
	context_object_name = 'artist_profile_list'

	def get_queryset(self):
		return ArtistProfile.objects.order_by('full_name')
    
class DetailView(generic.DetailView):
	model = ArtistProfile
	template_name = 'artistprofile/detail.html'
	context_object_name = 'artist_profile'

class CreateView(generic.edit.CreateView):
	model = ArtistProfile
	template_name = 'artistprofile/create_form.html'
	fields = '__all__'
