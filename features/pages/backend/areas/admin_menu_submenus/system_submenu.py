from features.core_config.backend.backend_locators import *
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.system_submenu_links import *


class SystemSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT['strategy'], ADMIN_MENU_ROOT['locator'])
        self.system_import = Import(SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR['strategy'],
                                    SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR['locator'])
        self.export = Export(SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR['strategy'],
                             SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR['locator'])
        self.import_export_tax_rates = ImportExportTaxRates(
            SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR['strategy'],
            SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR['locator'])
        self.import_history = ImportHistory(SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR['strategy'],
                                            SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR['locator'])
        self.integrations = Integrations(SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR['strategy'],
                                         SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR['locator'])
        self.cache_management = CacheManagement(SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR['strategy'],
                                                SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR['locator'])
        self.index_management = IndexManagement(SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR['strategy'],
                                                SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR['locator'])
        self.all_users = AllUsers(SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['strategy'],
                                  SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['locator'])
        self.locked_users = LockedUsers(SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['strategy'],
                                        SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['locator'])
        self.user_roles = UserRoles(SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR['strategy'],
                                    SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR['locator'])
        self.bulk_actions = BulkActions(SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR['strategy'],
                                        SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR['locator'])
        self.notifications = Notifications(SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR['strategy'],
                                           SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR['locator'])
        self.custom_variables = CustomVariables(SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR['strategy'],
                                                SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR['locator'])
        self.manage_encryption_key = ManageEncryptionKey(
            SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR['strategy'],
            SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR['locator'])
