from extras.plugins import PluginMenuItem, PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

credentiallist_buttons = [
    PluginMenuButton(
        link='plugins:netbox_credentials:credential_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN,
    ),
    PluginMenuButton(
        link='plugins:netbox_credentials:credential_import',
        title='Add',
        icon_class='mdi mdi-upload',
        color=ButtonColorChoices.CYAN,
    ),
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_credentials:credential_list',
        link_text='Credentials',
        buttons=credentiallist_buttons,
    ),
)
