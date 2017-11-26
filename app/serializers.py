from rest_framework import serializers

from app.models import Content


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'

