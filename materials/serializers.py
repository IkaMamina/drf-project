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


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer()

    def get_count_lesson(self, course):
        return Course.objects.filter(lesson=course.lesson).count()

    class Meta:
        model = Course
        fields = ("name", "description", "preview", "count_lesson")


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
