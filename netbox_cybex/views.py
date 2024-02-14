from netbox.views import generic
from . import filtersets, forms, models, tables


class CredentialView(generic.ObjectView):
    queryset = models.Credential.objects.all()
    template_name = 'netbox_cybex/credential.html'


class CredentialListView(generic.ObjectListView):
    queryset = models.Credential.objects.all()
    table = tables.CredentialTable
    filterset = filtersets.CredentialFilterSet
    filterset_form = forms.CredentialFilterForm


class CredentialEditView(generic.ObjectEditView):
    queryset = models.Credential.objects.all()
    form = forms.CredentialForm
    template_name = 'netbox_cybex/credential_edit.html'

class CredentialDeleteView(generic.ObjectDeleteView):
    queryset = models.Credential.objects.all()


class CredentialBulkImportView(generic.BulkImportView):
    queryset = models.Credential.objects.all()
    model_form = forms.CredentialImportForm


class CredentialBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Credential.objects.all()
    filterset = filtersets.CredentialFilterSet
    table = tables.CredentialTable
