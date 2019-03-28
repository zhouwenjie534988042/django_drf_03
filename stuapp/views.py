from stuapp.models import Actor
from rest_framework.viewsets import ModelViewSet

from stuapp.serializers import ActorSerializer


class ActorListView(ModelViewSet):
    """
    查询所有演员信息、增加演员信息、修改、删除操作
    """
    queryset = Actor.objects.all()

    serializer_class = ActorSerializer

