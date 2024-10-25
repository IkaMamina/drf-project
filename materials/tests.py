from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@test.ru")
        self.course = Course.objects.create(name="Первый курс", description="Основы программирования")
        self.lesson = Lesson.objects.create(name="Установка пайтон", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lessons_retrieve(self):
        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        responce = self.client.get(url)
        data = responce.json()

        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lessons_create(self):
        url = reverse("materials:lessons_create")
        data = {
            "name": "Django"
        }
        responce = self.client.post(url, data)

        self.assertEqual(
            responce.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lessons_update(self):
        url = reverse("materials:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "Django"
        }
        responce = self.client.patch(url, data)
        data = responce.json()

        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Django"
        )

    def test_lessons_delete(self):
        url = reverse("materials:lessons_delete", args=(self.lesson.pk,))
        responce = self.client.delete(url)

        self.assertEqual(
            responce.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lessons_list(self):
        url = reverse("materials:lessons_list")
        responce = self.client.get(url)

        self.assertEqual(
            responce.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            responce.data,
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 4, 'name': 'Установка пайтон', 'description': None, 'preview': None, 'link_video': None,
                 'course': 3, 'owner': 3}]}
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@test.ru")
        self.course = Course.objects.create(name="Первый курс", description="Основы программирования")
        self.lesson = Lesson.objects.create(name="Установка пайтон", course=self.course, owner=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        # Subscription.objects.all().delete()
        url = reverse("materials:subscription_create")
        data = {
            "course": self.course.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Подписка отключена'})
