# Generated by Django 2.2.16 on 2022-11-19 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0017_auto_20221119_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['name']},
        ),
    ]
