import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import columns, NetBoxTable

from .models import Credential


class CredentialTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = Credential
        fields = ('pk', 'id', 'service_type', 'parent', 'username', 'password', 'comments', 'actions')
        default_columns = ('service_type', 'parent', 'username', 'password')

    service_type = tables.Column(
        verbose_name=_('Service Type'),
        linkify=True
    )

    parent = tables.Column(
        verbose_name=_('Parent'),
        linkify=True,
        order_by=('device', 'virtual_machine')
    )

