from rest_framework import serializers
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, )

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password')


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


    class Meta:
        fields = ('id', 'username', 'password')


class TokenSerializer(serializers.Serializer):

    token = serializers.CharField(required=True)

    class Meta:
        fields = ('token')
