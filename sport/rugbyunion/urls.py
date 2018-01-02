from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import RugbyCalendar, RugbyCompetition

app_name = 'rugbyunion'

urlpatterns = [
    url(r'^monthly/$', RugbyCalendar.as_view(), name='monthly'),
    url(r'^competitions/$', RugbyCompetition.as_view(), name='competition'),
    #url(r'^scorecard/(?P<pk>\d+)/$', CricketDetail.as_view(), name='cricket-scorecard'),
]
