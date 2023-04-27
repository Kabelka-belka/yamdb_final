from django.forms import ValidationError
from django.utils import timezone


def yearvalidate(value):
    time = timezone.now().year
    if value > time:
        raise ValidationError(
            f'Указанный год "{value}" ещё не наступил!'
        )
