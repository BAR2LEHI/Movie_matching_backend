from rest_framework import viewsets, status
from movies.models import Movie, Genre, GenreToArtWork, Like
from users.models import User
from rest_framework.decorators import action
from .serializers import MovieSerializer, GenreSerializer, UserSerializer, CreateUserSerializer, LikeSerializer, PreferencesSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample


@extend_schema(tags=['Movies'])
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all().order_by('release_date')
    serializer_class = MovieSerializer

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=[IsAuthenticated,]
    )
    def like(self, request, pk):
        if request.method == 'POST':
            data = {
                'user': request.user.pk,
                'movie': pk
            }
            serializer = LikeSerializer(data=data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        obj = Like.objects.filter(
            user=request.user.pk,
            movie=pk
        )
        if not obj:
            return Response({'detail': 'У вас не стоял лайк на данный фильм'})
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['Genres'])
class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@extend_schema(tags=['Users'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,] #Написать пермишен

    @extend_schema(
        request=PreferencesSerializer,
        responses=UserSerializer
    )
    @action(
        methods=['POST', 'PATCH'],
        detail=True
    )
    def preferences(self, request, pk):
        if request.method == 'POST':
            for genre in request.data['genre']:
                data = {
                    'user': pk,
                    'genre': genre
                }
                serializer = PreferencesSerializer(
                    data=data, context={'request': request}
                )
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = UserSerializer(request.user, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return self.serializer_class
