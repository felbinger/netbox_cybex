from django.utils.translation import gettext as _
from extras.plugins import PluginMenuItem, PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


credentiallist_buttons = [
    PluginMenuButton(
        link='plugins:netbox_cybex:credential_add',
        title=_('Add'),
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN,
    ),
    PluginMenuButton(
        link='plugins:netbox_cybex:credential_import',
        title=_('Import'),
        icon_class='mdi mdi-upload',
        color=ButtonColorChoices.CYAN,
    ),
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_cybex:credential_list',
        link_text=_('Credentials'),
        buttons=credentiallist_buttons,
    ),
)
