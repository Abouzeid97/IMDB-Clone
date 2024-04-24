from django.contrib import admin
from .models import Watchlist, StreamPlatform, Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("rating", "watchlist")

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("title", "id")

class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(StreamPlatform, StreamPlatformAdmin)
admin.site.register(Review, ReviewAdmin)