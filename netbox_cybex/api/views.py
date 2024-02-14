from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import CredentialSerializer


class CredentialViewSet(NetBoxModelViewSet):
    queryset = models.Credential.objects.prefetch_related('tags')
    serializer_class = CredentialSerializer
