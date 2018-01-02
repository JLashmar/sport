from django.contrib import admin
from .models import Country_Data
# Register your models here.

@admin.register(Country_Data)
class CountryCreation(admin.ModelAdmin):
    list_display = ('name', 'country_slug')
    prepopulated_fields = {'country_slug': ('name',)}
