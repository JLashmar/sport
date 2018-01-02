from django.conf.urls import url, include
from . import views as articles_views
from django.views.generic import TemplateView

app_name = 'articles'

urlpatterns = [
    url(r'^(?P<sport_slug>[-_\w]+)/(?P<slug>[-_\w]+)/$', articles_views.DetailView.as_view(), name='detail'),
    url(r'^(?P<sport_slug>[-_\w]+)/(?P<country_slug>[-_\w]+)$', articles_views.CountryView.as_view(), name='country'),
    url(r'^', articles_views.IndexView.as_view(), name='index'),
]
