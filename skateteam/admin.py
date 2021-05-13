from django.contrib import admin
from .models import Skateteam, Teamcat

# Register your models here.


class SkateteamAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'teamcat',
        'rating',
        'image',
    )

    ordering = ('sku',)


class TeamcatAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Skateteam, SkateteamAdmin)
admin.site.register(Teamcat, TeamcatAdmin)
