import features.core_config.backend.backend_locators as bl
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
from features.pages.backend.fields.submenu_link import SubmenuLink
from stere.areas import Area
from stere.fields import Root, Link
from typing import List


class SystemSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT[STRATEGY_KEY], bl.ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.system_import = SubmenuLink(bl.SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR[STRATEGY_KEY],
                                    bl.SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR[LOCATOR_KEY])
        self.export = SubmenuLink(bl.SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR[STRATEGY_KEY],
                             bl.SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR[LOCATOR_KEY])
        self.import_export_tax_rates = SubmenuLink(
            bl.SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR[STRATEGY_KEY],
            bl.SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR[LOCATOR_KEY])
        self.import_history = SubmenuLink(bl.SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR[STRATEGY_KEY],
                                            bl.SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR[LOCATOR_KEY])
        self.integrations = SubmenuLink(bl.SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR[STRATEGY_KEY],
                                         bl.SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR[LOCATOR_KEY])
        self.cache_management = SubmenuLink(bl.SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR[STRATEGY_KEY],
                                                bl.SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR[LOCATOR_KEY])
        self.index_management = SubmenuLink(bl.SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR[STRATEGY_KEY],
                                                bl.SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR[LOCATOR_KEY])
        self.all_users = SubmenuLink(bl.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR[STRATEGY_KEY],
                                  bl.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR[LOCATOR_KEY])
        self.locked_users = SubmenuLink(bl.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR[STRATEGY_KEY],
                                        bl.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR[LOCATOR_KEY])
        self.user_roles = SubmenuLink(bl.SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR[STRATEGY_KEY],
                                    bl.SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR[LOCATOR_KEY])
        self.bulk_actions = SubmenuLink(bl.SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR[STRATEGY_KEY],
                                        bl.SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR[LOCATOR_KEY])
        self.notifications = SubmenuLink(bl.SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR[STRATEGY_KEY],
                                           bl.SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR[LOCATOR_KEY])
        self.custom_variables = SubmenuLink(bl.SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR[STRATEGY_KEY],
                                                bl.SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR[LOCATOR_KEY])
        self.manage_encryption_key = SubmenuLink(
            bl.SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR[STRATEGY_KEY],
            bl.SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR[LOCATOR_KEY])

    def links(self) -> List[Link]:
        return [
            self.system_import,
            self.export,
            self.import_export_tax_rates,
            self.import_history,
            self.integrations,
            self.cache_management,
            self.index_management,
            self.all_users,
            self.locked_users,
            self.user_roles,
            self.bulk_actions,
            self.notifications,
            self.custom_variables,
            self.manage_encryption_key
        ]
