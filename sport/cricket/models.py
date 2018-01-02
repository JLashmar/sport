from django.db import models
from datetime import datetime
from sports.models import Team, MatchType, Tier
from django_countries.fields import CountryField

# Create your models here.

class MonthlyView(models.Model):
    tour = models.ForeignKey('cricket.Tour', on_delete=models.CASCADE, related_name='tour_name')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class CricketPlayer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)
    international_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='cricket_international_team')
    domestic_teams = models.ManyToManyField('sports.Team', related_name='cricket_domestic_teams')

    def __str__(self):
        return self.first_name + ' ' + self.second_name

class Tour(models.Model):
    name = models.CharField(max_length=200)
    tier_level = models.ForeignKey('sports.Tier', on_delete=models.CASCADE)
    country = CountryField()
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    home_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='cricket_home_team')
    away_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='cricket_away_team')

    def __str__(self):
        return str(self.id)


class InningsScorecard(models.Model):
    fixture = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    runs = models.IntegerField(default=0)
    wides = models.IntegerField(default=0)
    no_ball = models.IntegerField(default=0)
    leg_byes = models.IntegerField(default=0)
    byes = models.IntegerField(default=0)
    penelty_runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.team)

class BattingDetail(models.Model):
    STATUS_CHOICES = (
        ('not out', 'not out'),
        ('bowled', 'bowled'),
        ('caught', 'caught'),
        ('lbw', 'lbw'),
        ('stumped', 'stumped'),
        ('ran-out', 'ran-out'),
        ('retired-hurt', 'retired-hurt'),
        ('retired-out', 'retired-out'),
        ('timed-out', 'timed-out'),
        ('handled-the-ball', 'handled-the-ball'),
    )
    innings = models.ForeignKey(InningsScorecard,on_delete=models.CASCADE,)
    player = models.ForeignKey(CricketPlayer, on_delete=models.CASCADE,)
    runs = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    strike_rate = models.IntegerField(default=0)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not out')
    bowled_by = models.ForeignKey('BowlingDetail', blank=True, null=True, on_delete=models.CASCADE, related_name='bowled_by')
    caught_by = models.ForeignKey(CricketPlayer, blank=True, null=True, on_delete=models.CASCADE, related_name='caught_by')

    def __str__(self):
        return str(self.player)

class BowlingDetail(models.Model):
    bowled = models.ForeignKey(BattingDetail, blank=True, null=True, on_delete=models.CASCADE, related_name='bowled')
    innings = models.ForeignKey(InningsScorecard, on_delete=models.CASCADE)
    player = models.ForeignKey(CricketPlayer, on_delete=models.CASCADE)
    runs = models.IntegerField(default=0)
    maidens = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs = models.FloatField(default=0.0)
    economy = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.player)

class FallofWicket(models.Model):
    match = models.ForeignKey(Match, blank=True, null=True, on_delete=models.CASCADE, related_name='match_wickets')
    innings = models.ForeignKey(InningsScorecard, blank=True, null=True, on_delete=models.CASCADE, related_name='innings_wickets')
    batsman = models.ForeignKey(BattingDetail, blank=True, null=True, on_delete=models.CASCADE, related_name='batsman_dismissed')
    wicket = models.IntegerField()
    runs = models.IntegerField()
