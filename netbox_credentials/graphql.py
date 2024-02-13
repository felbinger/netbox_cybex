from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import models


class CredentialType(NetBoxObjectType):

    class Meta:
        model = models.Credential
        fields = '__all__'


class Query(ObjectType):
    credential = ObjectField(CredentialType)
    credential_list = ObjectListField(CredentialType)


schema = Query
