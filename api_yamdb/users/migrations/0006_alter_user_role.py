# Generated by Django 4.1.3 on 2022-11-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_merge_20221118_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Аутентифицированный пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', help_text='Роль пользователя в системе', max_length=50, verbose_name='Роль'),
        ),
    ]
