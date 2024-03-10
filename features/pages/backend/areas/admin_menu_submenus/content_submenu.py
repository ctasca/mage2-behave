from features.core_config.backend.locators.admin_menu import ADMIN_MENU_ROOT
from features.core_config.backend.locators.admin_submenus import *
from stere.areas import Area
from stere.fields import Root, Link
from features.pages.backend.fields.submenu_link import SubmenuLink
from typing import List
from features.core_config.strategies import STRATEGY_KEY, LOCATOR_KEY


class ContentSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT[STRATEGY_KEY], ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.pages = SubmenuLink(CONTENT_SUBMENU_PAGES_LINK_LOCATOR[STRATEGY_KEY],
                                 CONTENT_SUBMENU_PAGES_LINK_LOCATOR[LOCATOR_KEY])
        self.blocks = SubmenuLink(CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR[STRATEGY_KEY],
                                  CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR[LOCATOR_KEY])
        self.widgets = SubmenuLink(CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR[STRATEGY_KEY],
                                   CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR[LOCATOR_KEY])
        self.templates = SubmenuLink(CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR[STRATEGY_KEY],
                                     CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR[LOCATOR_KEY])
        self.media_gallery = SubmenuLink(CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR[STRATEGY_KEY],
                                         CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR[LOCATOR_KEY])
        self.design_configuration = SubmenuLink(
            CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR[STRATEGY_KEY],
            CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR[LOCATOR_KEY])
        self.design_themes = SubmenuLink(CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR[STRATEGY_KEY],
                                         CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR[LOCATOR_KEY])
        self.design_schedule = SubmenuLink(CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR[STRATEGY_KEY],
                                           CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR[LOCATOR_KEY])

    def links(self) -> List[Link]:
        return [
            self.pages,
            self.blocks,
            self.widgets,
            self.templates,
            self.media_gallery,
            self.design_configuration,
            self.design_themes,
            self.design_schedule
        ]
