import django_filters

from movies.models import Movie, Genre, Preferences


class MovieFilter(django_filters.FilterSet):
    is_liked = django_filters.BooleanFilter(
        method='filter_is_liked'
    )
    title = django_filters.CharFilter(
        field_name='title'
    )
    genres = django_filters.AllValuesMultipleFilter(
        field_name='genre__name',
        lookup_expr='icontains'
    )
    preferences = django_filters.BooleanFilter(
        method='filter_preferences'
    )

    class Meta:
        model = Movie
        fields = (
            'title', 'genres', 
            'is_liked', 'preferences'
        )

    def filter_is_liked(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(
                art_user__user=self.request.user.id
            )
        return queryset
    
    def filter_preferences(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            genres = Genre.objects.filter(
                pk__in=[
                    pref.genre.id for pref in Preferences.objects.filter(
                        user=self.request.user
                    )
                ]
            )
            return queryset.filter(genre__in=genres)
        return queryset
