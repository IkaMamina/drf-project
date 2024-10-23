from rest_framework.serializers import ValidationError

link = ["youtube.com"]


def check_link(value):
    if not value.lower() in link:
        raise ValidationError("Использована запрещенная ссылка")
