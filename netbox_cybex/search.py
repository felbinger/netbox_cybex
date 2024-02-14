from netbox.search import SearchIndex, register_search
from .models import Credential

class CredentialIndex(SearchIndex):
    model = Credential

@register_search
class CredentialIndex(SearchIndex):
    model = Credential
    fields = (
        ('service_type', 100),
        ('username', 1000),
        ('password', 5000),
        ('comments', 5000),
    )
