from django.utils.translation import gettext_lazy as _
from utilities.forms.fields import CommentField, DynamicModelChoiceField, CSVModelChoiceField, DynamicModelMultipleChoiceField
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelFilterSetForm
from dcim.models import Device
from virtualization.models import VirtualMachine

from .models import Credential


class CredentialFilterForm(NetBoxModelFilterSetForm):
    model = Credential
    fieldsets = (
        (None, ('q', 'filter_id')),
        (_('Assignment'), ('device_id', 'virtual_machine_id')),
    )
    device_id = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label=_('Device'),
    )
    virtual_machine_id = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label=_('Virtual Machine'),
    )


class CredentialForm(NetBoxModelForm):
    class Meta:
        model = Credential
        fields = ('service_type', 'device', 'virtual_machine', 'username', 'password', 'comments', 'tags')

    device = DynamicModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=False,
        selector=True
    )
    virtual_machine = DynamicModelChoiceField(
        label=_('Virtual machine'),
        queryset=VirtualMachine.objects.all(),
        required=False,
        selector=True
    )
    comments = CommentField()


class CredentialImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Required if not assigned to a VM')
    )
    virtual_machine = CSVModelChoiceField(
        label=_('Virtual machine'),
        queryset=VirtualMachine.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Required if not assigned to a device')
    )

    class Meta:
        model = Credential
        fields = (
            'service_type', 'device', 'virtual_machine', 'username', 'password', 'comments', 'tags',
        )
