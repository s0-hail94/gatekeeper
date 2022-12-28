from rest_framework import serializers

class StatusSerializer(serializers.Serializer):
    message = serializers.CharField()