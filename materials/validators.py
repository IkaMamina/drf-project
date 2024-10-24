from rest_framework.serializers import ValidationError


def check_link(value):
    if "youtube.com" not in value:
        raise ValidationError("Использована запрещенная ссылка")
