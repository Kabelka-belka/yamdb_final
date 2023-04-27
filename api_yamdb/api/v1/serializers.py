from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
        )


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'name',
            'slug',
        )


class ReadTitlesSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(
        read_only=True,
    )
    genre = GenresSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category',
        )


class RecordTitlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category',
        )


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    def validate(self, data):
        if self.context['request'].method == 'POST':
            user = self.context['request'].user
            title_id = self.context['view'].kwargs['title_id']
            if Review.objects.filter(author=user, title_id=title_id).exists():
                raise serializers.ValidationError(
                    'Отзыв уже оставлен!'
                )
        return data

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'score',
            'pub_date',
            'title'
        )
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'review',
            'pub_date'
        )
        model = Comment


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def validate(self, data):
        username = data['username']
        email = data['email']
        if username == 'me':
            raise serializers.ValidationError(
                'Имя me является зарезервированым!'
            )
        if User.objects.filter(username=username, email=email).exists():
            return data
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                f'Имя {username} уже занято!'
            )
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                f'Пользователь с почтовым адресом {email} существует!'
            )
        return data


class SignUpConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate_username(self, value):
        get_object_or_404(User, username=value)
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        read_only_field = ('role',)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Этот email уже занят!')
        return value
