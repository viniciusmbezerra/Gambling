from django.contrib import admin

from .models import Bet, Concourse


@admin.register(Concourse)
class ConcourseAdmin(admin.ModelAdmin):
    ...

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    ...