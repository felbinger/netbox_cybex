from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Credential

class CredentialSerializer(NetBoxModelSerializer):

    class Meta:
        model = Credential
        fields = (
            'id', 'display', 'virtual_machine', 'service_type', 'username', 'password', 'comments',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
