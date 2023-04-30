from api.v1.filters import TitleFilter
from api.v1.permissions import (IsAdminOrAlloWGetOnlyPermission,
                                IsAdminOrSuperPermission,
                                IsAuthorModeratorAdminOrReadOnly)
from api.v1.serializers import (CategoriesSerializer, CommentSerializer,
                                GenresSerializer, ReadTitlesSerializer,
                                RecordTitlesSerializer, ReviewSerializer,
                                SignUpConfirmationSerializer, SignUpSerializer,
                                UserSerializer)
from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from reviews.models import Category, Genre, Review, Title
from users.models import User

from api_yamdb.settings import ADMIN_EMAIL


class CreateListDestroyViewset(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    pass


class CategoryViewSet(CreateListDestroyViewset):
    """
    Получить все категории из модели
    доступ:
    GET: Доступно без токена
    POST: ADMIN
    DEL: ADMIN
    """
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrAlloWGetOnlyPermission, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )
    lookup_field = 'slug'


class GenresViewSet(CreateListDestroyViewset):
    """
    Получить все жанры из модели
    доступ:
    GET: Доступно без токена
    POST: ADMIN
    DEL: ADMIN
    """
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminOrAlloWGetOnlyPermission, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)
    lookup_field = 'slug'


class TitelsViewSet(viewsets.ModelViewSet):
    """
    Получить все произведения из модели
    доступ:
    GET: Доступно без токена
    POST: ADMIN
    PATCH: ADMIN
    DEL: ADMIN
    """
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).order_by('name')
    permission_classes = (IsAdminOrAlloWGetOnlyPermission, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return ReadTitlesSerializer
        return RecordTitlesSerializer


@api_view(['POST'])
def sign_up_view(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user = User.objects.get_or_create(
        username=username,
        email=email,
    )
    token = Token.objects.get_or_create(user=user[0])
    try:
        send_mail(
            'Токен для регистрации',
            f'Ваш токен для продолжения регистрации: {token}',
            ADMIN_EMAIL,
            [email],
            fail_silently=False,
        )
    except Exception as error:
        user[0].delete
        token[0].delete
        raise Exception(error)
    return Response(serializer.data)


@api_view(['POST'])
def sign_up_confirmation_view(request):
    serializer = SignUpConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    confirmation_code = serializer.validated_data.get('confirmation_code')
    user = get_object_or_404(User, username=username)
    token = get_object_or_404(Token, user=user)
    if confirmation_code == token.key:
        refresh = RefreshToken.for_user(user)
        return Response(
            {'token': str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )
    return Response(
        {'token': 'Неверный токен регистрации!'},
        status=status.HTTP_400_BAD_REQUEST,
    )


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrSuperPermission,)
    lookup_field = 'username'

    @action(methods=['GET', 'PATCH'], detail=False,
            permission_classes=[IsAuthenticated])
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(role=user.role)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthorModeratorAdminOrReadOnly,
    )

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorModeratorAdminOrReadOnly,
    )

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review, id=self.kwargs.get('review_id'),
        )
        serializer.save(author=self.request.user, review=review)
