from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    """Конфигуратор админки."""
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'role',
        'bio',
    )
    search_fields = ('username', 'email')
    list_filter = ('role',)
    empty_value_display = '-пусто-'
    list_editable = ('role',)


admin.site.register(User, UserAdmin)
