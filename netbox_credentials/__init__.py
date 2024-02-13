from extras.plugins import PluginConfig

class NetBoxCredentialsConfig(PluginConfig):
    name = 'netbox_credentials'
    verbose_name = ' NetBox Credentials'
    description = 'Manage credentials in NetBox'
    version = '0.1'
    base_url = 'credentials'
    min_version = '3.4.0'

config = NetBoxCredentialsConfig