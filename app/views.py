from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from app.models import Content
from app.serializers import ContentSerializer


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer