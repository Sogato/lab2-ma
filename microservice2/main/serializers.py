from rest_framework import serializers
from .models import BD2


class BDSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, max_length=100)
    text = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)

    def create(self, validated_data):
        return BD2.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance
