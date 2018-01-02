from django.contrib import admin
from cricket.models import BattingDetail, BowlingDetail, CricketPlayer, Tour, Match, InningsScorecard, FallofWicket, MonthlyView
# Register your models here.

admin.site.register(CricketPlayer)
admin.site.register(MonthlyView)

admin.site.register(Tour)
admin.site.register(Match)
admin.site.register(InningsScorecard)

admin.site.register(BattingDetail)
admin.site.register(BowlingDetail)
admin.site.register(FallofWicket)
