from django.conf.urls import url, include
from django.views.generic import TemplateView

from cricket.views import CricketCalendar, CricketDetail, CricketCompetition
from cricket.models import MonthlyView

app_name = 'cricket'

urlpatterns = [
    url(r'^monthly/$', CricketCalendar.as_view(), name='monthly'),
    url(r'^scorecard/(?P<pk>\d+)/$', CricketDetail.as_view(), name='cricket-scorecard'),
    url(r'^competitions/$', CricketCompetition.as_view(), name='competition'),
]
