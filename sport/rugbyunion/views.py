from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView

# Create your views here.

from rugbyunion.models import Competition, CompetitionDetail, Match, RugbyPlayer, MatchScorecard, PlayerDetail, MonthlyView
from sports.models import Sport

class RugbyCalendar(ListView):
    template_name = "rugbyunion/monthly-view.html"
    context_object_name = 'monthly_view'

    def get_queryset(self):
        return MonthlyView.objects.all()

    def get_context_data(self):
        context = super(RugbyCalendar, self).get_context_data()
        context['country_selector'] = Competition.objects.all()
        context['match'] = Match.objects.all()
        context['sport_menu'] = get_object_or_404(Sport, sport_slug='rugbyunion')
        return context

class RugbyCompetition(ListView):
    template_name = "rugbyunion/competition.html"
    context_object_name = 'competition_view'

    def get_queryset(self):
        return Competition.objects.all()

    def get_context_data(self):
        context = super(RugbyCompetition, self).get_context_data()
        context['match'] = Match.objects.all()
        context['competition_info'] = CompetitionDetail.objects.all()
        context['sport_menu'] = get_object_or_404(Sport, sport_slug='rugbyunion')
        return context

class RugbyDetail(DetailView): #maybe change to a list view?
    model = Match
    template_name="rugby/rugby-scorecard.html"
    context_object_name='rugby_score_card'

    def get_context_data(self, **kwargs):
        context = super(RugbyDetail, self).get_context_data(**kwargs)
        context['competition'] = Competition.objects.all()
        context['competitiondetail'] = CompetitionDetail.objects.filter(id=self.object.pk)
        context['rugbyplayer'] = RugbyPlayer.objects.filter(id=self.object.pk)
        context['matchscorecard'] = MatchScorecard.objects.filter(id=self.object.pk)
        context['playerdetail'] = PlayerDetail.objects.filter(id=self.object.pk)
        return context
