from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import check_link


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    name = serializers.CharField(validators=[check_link])

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer()
    subscription = serializers.SerializerMethodField()

    def get_count_lesson(self, course):
        return Course.objects.filter(lesson=course.lesson).count()

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exists()

    class Meta:
        model = Course
        fields = ("name", "description", "preview", "count_lesson", "subscription")
