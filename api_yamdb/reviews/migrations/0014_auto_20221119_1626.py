# Generated by Django 2.2.16 on 2022-11-19 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20221119_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='score',
        ),
    ]