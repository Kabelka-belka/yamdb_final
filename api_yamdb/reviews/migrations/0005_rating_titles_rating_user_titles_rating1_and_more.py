# Generated by Django 4.1.3 on 2022-11-16 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0004_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='titles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titlesRating', to='reviews.titles'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='titles',
            name='Rating1',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'titles')},
        ),
    ]
