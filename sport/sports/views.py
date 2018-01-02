from django.views.generic import ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404

#my stuff
from sports.models import Sport_Category, Sport, Team
from articles.models import Post
import datetime

class SportListView(ListView):
	template_name="sports/sport-home.html"
	context_object_name='sport_list'

	def get_queryset(self):
		self.sport = get_object_or_404(Sport, sport_slug=self.kwargs['sport_slug'])
		return Post.objects.filter(post_category=self.sport)

	def get_context_data(self, **kwargs):
		context = super(SportListView, self).get_context_data(**kwargs)
		context['country_selector'] = Post.objects.filter(post_category=self.sport)
		context['sport_menu'] = get_object_or_404(Sport, sport_slug=self.kwargs['sport_slug'])
		return context
