import redis
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from app.models import Content
from app.serializers import ContentSerializer
from surfind.settings import REDIS_POLL


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        conn = redis.Redis(connection_pool=REDIS_POLL)
        obj = serializer.save()
        conn.set(obj.id, 'Obj created  %s ' % obj)
        return obj