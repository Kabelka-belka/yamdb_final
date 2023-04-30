import csv

from django.core.management import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

CSVMODEL = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    'genre_title': 'genre_title.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


def renaming_titels_cvs(rom, model):
    rom['category_id'] = rom.pop('category')
    model.objects.bulk_create([model(**rom)])


def renaming_review_cvs(rom, model):
    rom['author_id'] = rom.pop('author')
    model.objects.bulk_create([model(**rom)])


def renaming_comment_cvs(rom, model):
    rom['author_id'] = rom.pop('author')
    model.objects.bulk_create([model(**rom)])


def renaming_genre_title_cvs(rom, model):
    del rom['id']
    genre = Genre.objects.get(id=rom['genre_id'])
    title = Title.objects.get(id=rom['title_id'])
    genre.titles.add(title)


class Command(BaseCommand):
    help = "Loads data from csv"

    def handle(self, *args, **options):
        self.stdout.write("Loading data")
        for model, cvs in CSVMODEL.items():
            if model != 'genre_title':
                model.objects.all().delete()
            with open(f'static/data/{cvs}', encoding='utf-8') as opencvs:
                dictreadercvs = csv.DictReader(opencvs)
                for rom in dictreadercvs:
                    options = {
                        Title: renaming_titels_cvs,
                        Review: renaming_review_cvs,
                        Comment: renaming_comment_cvs,
                        'genre_title': renaming_genre_title_cvs
                    }
                    args = (rom, model)
                    operation = options.get(model)
                    if operation:
                        operation(*args)
                    else:
                        model.objects.bulk_create([model(**rom)])
        print("Loading database is complete")
