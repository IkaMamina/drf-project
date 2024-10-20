from rest_framework.serializers import ModelSerializer

from users.models import Pay, User


class PaySerializer(ModelSerializer):
    class Meta:
        model = Pay
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
