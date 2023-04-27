from django.contrib import admin

from .models import Category, Genre, Review, Title


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    search_fields = ('name',)
    empty_value_display = '-empty-'


@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    search_fields = ('name',)
    empty_value_display = '-empty-'


@admin.register(Title)
class TitlesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
    )
    search_fields = ('name', 'category',)
    list_filter = ('name', 'category',)
    empty_value_display = '-empty-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'text',
        'score',
    )
    search_fields = ('author', 'pub_date',)
    list_filter = ('author', 'pub_date',)
    empty_value_display = '-empty-'
