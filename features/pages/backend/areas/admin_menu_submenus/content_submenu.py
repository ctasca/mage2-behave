from stere.areas import Area
from stere.fields import Root, Link
from features.pages.backend.fields.submenu_link import SubmenuLink
from typing import List
from features.core_config.locators import STRATEGY_KEY, LOCATOR_KEY
import features.core_config.backend.backend_locators as bl


class ContentSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT[STRATEGY_KEY], bl.ADMIN_MENU_ROOT[LOCATOR_KEY])
        self.pages = SubmenuLink(bl.CONTENT_SUBMENU_PAGES_LINK_LOCATOR[STRATEGY_KEY],
                           bl.CONTENT_SUBMENU_PAGES_LINK_LOCATOR[LOCATOR_KEY])
        self.blocks = SubmenuLink(bl.CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR[STRATEGY_KEY],
                             bl.CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR[LOCATOR_KEY])
        self.widgets = SubmenuLink(bl.CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR[STRATEGY_KEY],
                               bl.CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR[LOCATOR_KEY])
        self.templates = SubmenuLink(bl.CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR[STRATEGY_KEY],
                                   bl.CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR[LOCATOR_KEY])
        self.media_gallery = SubmenuLink(bl.CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR[STRATEGY_KEY],
                                          bl.CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR[LOCATOR_KEY])
        self.design_configuration = SubmenuLink(
            bl.CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR[STRATEGY_KEY],
            bl.CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR[LOCATOR_KEY])
        self.design_themes = SubmenuLink(bl.CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR[STRATEGY_KEY],
                                          bl.CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR[LOCATOR_KEY])
        self.design_schedule = SubmenuLink(bl.CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR[STRATEGY_KEY],
                                              bl.CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR[LOCATOR_KEY])

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
