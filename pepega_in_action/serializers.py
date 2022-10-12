from rest_framework import serializers

class MemesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()