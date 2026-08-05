from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from .filters import AdvertisementFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

    def perform_destroy(self, instance):
        if self.request.user.is_staff:
            instance.delete()
            return
        if instance.creator != self.request.user:
            raise PermissionDenied('Недостаточно прав.' \
            'Вы пытаетесь удалить чужое обьявление!')
        instance.delete()

    def perform_update(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
            return
        if serializer.instance.creator != self.request.user:
            raise PermissionDenied('Недостаточно прав.' \
            'Вы пытаетесь обновить чужое обьявляение!')
        serializer.save()
