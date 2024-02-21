import features.core_config.all as config
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.system_submenu_links import *


class SystemSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(config.ADMIN_MENU_ROOT['strategy'], config.ADMIN_MENU_ROOT['locator'])
        self.system_import = Import(config.SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR['strategy'],
                                    config.SYSTEM_SUBMENU_IMPORT_LINK_LOCATOR['locator'])
        self.export = Export(config.SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR['strategy'],
                             config.SYSTEM_SUBMENU_EXPORT_LINK_LOCATOR['locator'])
        self.import_export_tax_rates = ImportExportTaxRates(
            config.SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR['strategy'],
            config.SYSTEM_SUBMENU_IMPORT_EXPORT_LINK_LOCATOR['locator'])
        self.import_history = ImportHistory(config.SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR['strategy'],
                                            config.SYSTEM_SUBMENU_IMPORT_HISTORY_LINK_LOCATOR['locator'])
        self.integrations = Integrations(config.SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR['strategy'],
                                         config.SYSTEM_SUBMENU_INTEGRATIONS_LINK_LOCATOR['locator'])
        self.cache_management = CacheManagement(config.SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR['strategy'],
                                                config.SYSTEM_SUBMENU_CACHE_MANAGEMENT_LINK_LOCATOR['locator'])
        self.index_management = IndexManagement(config.SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR['strategy'],
                                                config.SYSTEM_SUBMENU_INDEX_MANAGEMENT_LINK_LOCATOR['locator'])
        self.all_users = AllUsers(config.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['strategy'],
                                  config.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['locator'])
        self.locked_users = LockedUsers(config.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['strategy'],
                                        config.SYSTEM_SUBMENU_ALL_USERS_LINK_LOCATOR['locator'])
        self.user_roles = UserRoles(config.SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR['strategy'],
                                    config.SYSTEM_SUBMENU_USER_ROLES_LINK_LOCATOR['locator'])
        self.bulk_actions = BulkActions(config.SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR['strategy'],
                                        config.SYSTEM_SUBMENU_BULK_ACTIONS_LINK_LOCATOR['locator'])
        self.notifications = Notifications(config.SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR['strategy'],
                                           config.SYSTEM_SUBMENU_NOTIFICATIONS_LINK_LOCATOR['locator'])
        self.custom_variables = CustomVariables(config.SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR['strategy'],
                                                config.SYSTEM_SUBMENU_CUSTOM_VARIABLES_LINK_LOCATOR['locator'])
        self.manage_encryption_key = ManageEncryptionKey(
            config.SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR['strategy'],
            config.SYSTEM_SUBMENU_MANAGE_ENCRYPTION_KEY_LINK_LOCATOR['locator'])
