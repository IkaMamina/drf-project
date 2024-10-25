from django.db import models

from config import settings

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание курса", help_text="Укажите описание курса"
    )
    preview = models.ImageField(
        **NULLABLE, verbose_name="Превью курса", help_text="Загрузите превью курса"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Пользователь",
        help_text="Укажите пользователя"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание урока", help_text="Укажите описание урока"
    )
    preview = models.ImageField(
        **NULLABLE, verbose_name="Превью урока", help_text="Загрузите превью урока"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Название курса",
        help_text="Укажите название курса"
    )
    link_video = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Пользователь",
        help_text="Укажите пользователя"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    subscription = models.BooleanField(default=False, verbose_name='Признак подписки')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
