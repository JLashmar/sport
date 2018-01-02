from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import DetailView, ListView
# Create your views here.

from cricket.models import Tour, Match, InningsScorecard, BattingDetail, BowlingDetail, CricketPlayer, FallofWicket, MonthlyView
from sports.models import Sport


class CricketCalendar(ListView):
    template_name = "cricket/monthly-view.html"
    context_object_name = 'monthly_view'

    def get_queryset(self):
        return MonthlyView.objects.all()

    def get_context_data(self):
        context = super(CricketCalendar, self).get_context_data()
        context['cricket_tour'] = Tour.objects.all()
        context['match'] = Match.objects.all()
        context['sport_menu'] = get_object_or_404(Sport, sport_slug='cricket')
        return context

class CricketCompetition(ListView):
    template_name = "cricket/competition.html"
    context_object_name = 'competition_view'

    def get_queryset(self):
        return Tour.objects.all()

    def get_context_data(self):
        context = super(CricketCompetition, self).get_context_data()
        context['match'] = Match.objects.all()
        #context['competition_info'] = CompetitionDetail.objects.all()
        context['sport_menu'] = get_object_or_404(Sport, sport_slug='cricket')
        return context


class CricketDetail(DetailView):
    model = Match
    template_name = "cricket/cricket_scorecard.html"
    context_object_name = 'cricket_score_card'

    def get_context_data(self, **kwargs):
        context = super(CricketDetail, self).get_context_data(**kwargs)
        context['tour'] = Tour.objects.all()
        context['inningsscorecard'] = InningsScorecard.objects.filter(id=self.object.pk)
        context['battingdetail'] = BattingDetail.objects.filter(id=self.object.pk)
        context['bowlingdetail'] = BowlingDetail.objects.filter(id=self.object.pk)
        context['cricketplayer'] = CricketPlayer.objects.filter(id=self.object.pk)
        context['fallofwicket'] = FallofWicket.objects.filter(id=self.object.pk)
        context['sport_menu'] = get_object_or_404(Sport, sport_slug='cricket')
        return context

    def get_object(self):

        obj = get_object_or_404(
            self.model,
            pk=self.kwargs['pk'])

        return obj
