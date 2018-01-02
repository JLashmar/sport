from django.contrib import admin
from rugbyunion.models import MonthlyView, Competition, CompetitionDetail, RugbyPlayer, Match, MatchScorecard, PlayerDetail
# Register your models here.

admin.site.register(MonthlyView)
admin.site.register(Competition)
admin.site.register(RugbyPlayer)
admin.site.register(Match)
admin.site.register(MatchScorecard)
admin.site.register(PlayerDetail)

@admin.register(CompetitionDetail)
class CompetitionDetail(admin.ModelAdmin):
    list_display = ('competition', 'team', 'games_played', 'won', 'lost', 'drawn', 'total_points')
