import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from dcim.models import Device, Interface, Region, Site, SiteGroup
from netbox.filtersets import ChangeLoggedModelFilterSet, OrganizationalModelFilterSet, NetBoxModelFilterSet
from virtualization.models import VirtualMachine, VMInterface
from .models import *


class CredentialFilterSet(NetBoxModelFilterSet):
    device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        label=_('Device (ID)'),
    )
    device = django_filters.ModelMultipleChoiceFilter(
        field_name='device__name',
        queryset=Device.objects.all(),
        to_field_name='name',
        label=_('Device (name)'),
    )
    virtual_machine_id = django_filters.ModelMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        label=_('Virtual machine (ID)'),
    )
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        field_name='virtual_machine__name',
        queryset=VirtualMachine.objects.all(),
        to_field_name='name',
        label=_('Virtual machine (name)'),
    )

    class Meta:
        model = Credential
        fields = ['id', 'service_type', 'username']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(service_type__icontains=value) | Q(username__icontains=value)
        return queryset.filter(qs_filter)
