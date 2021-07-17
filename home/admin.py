from django.contrib import admin

from .models import Mission, MissionPost, Rocket, Timeline, MissionImage

admin.site.register(MissionPost)
admin.site.register(Timeline)
admin.site.register(Rocket)


class MissionImageAdmin(admin.StackedInline):
    model = MissionImage


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    inlines = [MissionImageAdmin]

    class Meta:
        model = Mission


@admin.register(MissionImage)
class MissionImageAdmin(admin.ModelAdmin):
    pass
