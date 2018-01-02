from django.contrib import admin
from .models import Sport_Category, Sport, Team, Gender, Tier, MatchType

@admin.register(Sport_Category)
class SportCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_slug')
    prepopulated_fields = {'category_slug': ('name',)}


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'sport_slug': ('name',)}

@admin.register(Gender)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('gender', 'pk' )

@admin.register(Tier)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('tier_level', 'pk')

@admin.register(MatchType)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'sport')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('sport', 'team_name', 'nation', 'gender', 'tier')

#admin.site.register(Sport_Category)
#admin.site.register(Sport)
