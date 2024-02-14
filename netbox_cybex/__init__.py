from extras.plugins import PluginConfig

class NetBoxCybExConfig(PluginConfig):
    name = 'netbox_cybex'
    verbose_name = ' NetBox CybEx'
    description = 'Features for cyber exercises in NetBox'
    version = '0.1'
    base_url = 'cybex'
    min_version = '3.4.0'

config = NetBoxCybExConfig
