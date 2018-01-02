from django.db import models
from django.db.models import permalink
from django.urls import reverse
from sports.models import Sport, Sport_Category, Team
from django_countries.fields import CountryField
from embed_video.fields import EmbedVideoField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    post_slug = models.SlugField(max_length=100, unique=True)
    short_description = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField()
    headline_image = models.ImageField(blank=True, null=True)
    post_image = models.ImageField(blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    post_category = models.ForeignKey('sports.Sport', related_name='post_category',on_delete=models.CASCADE)
    team_a = models.ForeignKey('sports.Team', related_name='first_team', on_delete=models.CASCADE)
    #team_a_country = CountryField()
    team_b = models.ForeignKey('sports.Team', related_name='second_team', on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True, null=True)
    #listed_country = combined teama and teamb nation

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'sport_slug':self.post_category.sport_slug, 'slug':self.post_slug})

class VideoNews(models.Model):
    title = models.CharField(max_length=100, unique=True)
    related_post = models.ForeignKey('Post', blank=True, null=True, on_delete=models.CASCADE)
    link = models.URLField()
    video = EmbedVideoField()  # same like models.URLField()

    def __str__(self):
        return self.title
