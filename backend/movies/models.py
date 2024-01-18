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


class Genre(models.Model):
    name = models.CharField(
        max_length=54
    )


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_art'
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='art_user'
    )
    date = models.DateTimeField(
        auto_now=True
    )


class GenreToArtWork(models.Model):
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.CASCADE,
        related_name='genre_art'
    )
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.CASCADE,
        related_name='art_genre'
    )


class Preferences(models.Model):
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.CASCADE,
        related_name='genres'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )


