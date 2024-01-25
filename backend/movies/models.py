from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(
        verbose_name='Название'
    )
    poster = models.ImageField(
        upload_to='posters/',
        verbose_name='Постер',
        null=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    rating_imdb = models.IntegerField(
        verbose_name='Рейтинг IMDB',
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    content_rating = models.CharField(
        verbose_name='Возрастной рейтинг'
    )
    budget = models.IntegerField(
        verbose_name='Бюджет',
        validators=[MinValueValidator(0), MaxValueValidator(1000000000)]
    )
    revenue = models.IntegerField(
        verbose_name='Сборы',
        validators=[MinValueValidator(0), MaxValueValidator(8000000000)]
    )
    genre = models.ManyToManyField(
        'Genre',
        db_index=True,
        through='GenreToArtWork',
        verbose_name='Жанры Фильма'
    )
    release_date = models.DateField(
        verbose_name='Дата релиза',
        db_index=True
    )
    timing = models.CharField(
        verbose_name='Хронометраж'
    )

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(
        max_length=54,
        verbose_name='Название жанра'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_art',
        verbose_name='Пользователь'
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='art_user',
        verbose_name='Жанр'
    )
    date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата лайка'
    )

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f'Лайк {self.user} на {self.movie}'


class GenreToArtWork(models.Model):
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.CASCADE,
        related_name='genre_art',
        verbose_name='Жанр'
    )
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.CASCADE,
        related_name='art_genre',
        verbose_name='Фильм'
    )

    class Meta:
        verbose_name = 'Жанр у фильмов'
        verbose_name_plural = 'Жанры у фильмов'

    def __str__(self):
        return f'{self.genre} у фильма {self.movie}'


class Preferences(models.Model):
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.CASCADE,
        related_name='genres',
        verbose_name='Жанр'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Предпочтение'
        verbose_name_plural = 'предпочтения'

    def __str__(self):
        return f'{self.user} предпочитает жанр {self.genre}'
