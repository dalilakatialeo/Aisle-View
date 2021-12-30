from rest_framework.serializers import ModelSerializer

from .models import CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('firstname')