from django.contrib import admin

from .models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    list_display = (
        'title',
        'description',
        'rating_imdb',
        'content_rating',
        'release_date',
        'timing',
    )
    search_fields = (
        'title',
        'release_date'
    )
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


