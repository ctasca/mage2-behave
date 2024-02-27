import features.core_config.backend.backend_locators as bl
from features.pages.backend.fields.system_submenu_links import *
from stere.areas import Area
from stere.fields import Root
from typing import List


class SystemSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT['strategy'], bl.ADMIN_MENU_ROOT['locator'])
        self.system_import = Import(bl.SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR['strategy'],
                                    bl.SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR['locator'])
        self.export = Export(bl.SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR['strategy'],
                             bl.SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR['locator'])
        self.import_export_tax_rates = ImportExportTaxRates(
            bl.SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR['strategy'],
            bl.SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR['locator'])
        self.import_history = ImportHistory(bl.SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR['strategy'],
                                            bl.SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR['locator'])
        self.integrations = Integrations(bl.SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR['strategy'],
                                         bl.SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR['locator'])
        self.cache_management = CacheManagement(bl.SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR['strategy'],
                                                bl.SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR['locator'])
        self.index_management = IndexManagement(bl.SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR['strategy'],
                                                bl.SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR['locator'])
        self.all_users = AllUsers(bl.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['strategy'],
                                  bl.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['locator'])
        self.locked_users = LockedUsers(bl.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['strategy'],
                                        bl.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['locator'])
        self.user_roles = UserRoles(bl.SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR['strategy'],
                                    bl.SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR['locator'])
        self.bulk_actions = BulkActions(bl.SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR['strategy'],
                                        bl.SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR['locator'])
        self.notifications = Notifications(bl.SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR['strategy'],
                                           bl.SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR['locator'])
        self.custom_variables = CustomVariables(bl.SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR['strategy'],
                                                bl.SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR['locator'])
        self.manage_encryption_key = ManageEncryptionKey(
            bl.SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR['strategy'],
            bl.SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR['locator'])

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
