from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        (USER, 'Аутентифицированный пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    )
    username = models.CharField(
        'Имя пользователя',
        help_text=('Имя пользователя'),
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        help_text=('Введите email'),
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(
        'Имя',
        help_text=('Введите имя'),
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        'Фамилия',
        help_text=('Введите фамилию'),
        max_length=150,
        blank=True,
    )
    role = models.CharField(
        'Роль',
        help_text=('Роль пользователя в системе'),
        choices=ROLE_CHOICES,
        default=USER,
        max_length=50,
    )
    bio = models.TextField(
        help_text=('О себе'),
        blank=True,
    )

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
