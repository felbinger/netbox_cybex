from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (
    path('credential/', views.CredentialListView.as_view(), name='credential_list'),
    path('credential/add/', views.CredentialEditView.as_view(), name='credential_add'),
    path('credential/import/', views.CredentialBulkImportView.as_view(), name='credential_import'),
    path('credential/<int:pk>/', views.CredentialView.as_view(), name='credential'),
    path('credential/<int:pk>/edit/', views.CredentialEditView.as_view(), name='credential_edit'),
    path('credential/<int:pk>/delete/', views.CredentialDeleteView.as_view(), name='credential_delete'),

    path('credential/delete/', views.CredentialBulkDeleteView.as_view(), name='credential_bulk_delete'),

    path('credential/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='credential_changelog', kwargs={
        'model': models.Credential
    }),

)
