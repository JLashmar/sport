from django.conf.urls import url, include
from . import views as sports_views
from django.views.generic import TemplateView

#from monthly_view.views import CricketCalendar
from cricket import views as cricket
from sports.views import SportListView

app_name = 'sports'

urlpatterns = [
    url(r'^$', sports_views.SportListView.as_view(), name='sport-home'),
    #url(r'^monthly-view/$', cricket.CricketCalendar.as_view(), name='monthly-view'),
    url(r'^(?P<category_slug>[-_\w]+)/$', sports_views.ListView.as_view(), name='sport-category'),
]
