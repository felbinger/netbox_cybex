from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class Credential(NetBoxModel):
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='credentials',
        verbose_name=_('device'),
        null=True,
        blank=True
    )
    virtual_machine = models.ForeignKey(
        to='virtualization.VirtualMachine',
        on_delete=models.CASCADE,
        related_name='credentials',
        null=True,
        blank=True
    )
    # e.g. Telnet, SSH, HTTP, RDP, VNC, ...
    service_type = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('plugins:netbox_cybex:credential', args=[self.pk])

    @property
    def parent(self):
        return self.device or self.virtual_machine

    def clean(self):
        super().clean()

        # A Service must belong to a Device *or* to a VirtualMachine
        if self.device and self.virtual_machine:
            raise ValidationError(_("A credential cannot be associated with both a device and a virtual machine."))
        if not self.device and not self.virtual_machine:
            raise ValidationError(_("A credential must be associated with either a device or a virtual machine."))
