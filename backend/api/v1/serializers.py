from rest_framework import serializers
from movies.models import Movie, Genre, Like, Preferences, GenreToArtWork
from movies.models import User
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            'id', 'name'
        )


class MovieSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 
            'poster', 'description',
            'rating_imdb', 'content_rating',
            'budget', 'revenue',
            'genre', 'release_date',
            'timing', 'is_liked'
        )
    
    def get_is_liked(self, obj) -> bool:
        user = self.context.get('request').user
        return user.is_authenticated and Like.objects.filter(
            movie=obj,
            user=user
        ).exists()


@extend_schema_serializer( 
    examples = [
         OpenApiExample(
            'Valid example 1',
            summary='short summary',
            value={
                'genre': [1, 2, 3]
            },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class PreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preferences
        fields = (
            'id', 'user',
            'genre'
        )

    def validate_genre(self, data):
        if Preferences.objects.filter(
            genre=data.id,
            user=self.context.get('request').user.id
        ).exists():
            raise serializers.ValidationError(
                f'Жанр с id={data.id} уже в предпочтениях'
            )
        
        return data


class UserSerializer(serializers.ModelSerializer):
    preferences = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'username',
            'email', 'is_active',
            'is_staff', 'created_at',
            'updated_at', 'preferences'
        )
    
    def get_preferences(self, obj) -> list[Genre]:
        data = []
        genres = Genre.objects.filter(
            genres__user=self.context.get('request').user
        )
        for genre in genres:
            serializer = GenreSerializer(
                genre, context={'request': self.context.get('request')}
            )
            data.append(serializer.data)
        return data
        


class LikeRepresentationSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    user = UserSerializer()

    class Meta:
        model = Like
        fields = (
            'id', 'user',
            'movie', 'date'
        )


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = (
            'id', 'user',
            'movie', 'date'
        )
    
    def validate(self, data):
        movie = data['movie']
        user = data['user']
        if Like.objects.filter(
            movie=movie,
            user=user
        ).exists():
            raise serializers.ValidationError(
                'Лайк на этот фильм уже стоит.'
            )
        return data

    def to_representation(self, instance):
        return LikeRepresentationSerializer(
            instance, context={'request': self.context.get('request')}
        ).data



class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email',
            'password'
        )

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        data = super(CreateUserSerializer, self).to_representation(instance)
        data.pop('password')
        return data
