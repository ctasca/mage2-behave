from features.core_config.backend.backend_locators import *
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.content_submenu_links import *
from typing import List


class ContentSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(ADMIN_MENU_ROOT['strategy'], ADMIN_MENU_ROOT['locator'])
        self.pages = Pages(CONTENT_SUBMENU_PAGES_LINK_LOCATOR['strategy'],
                           CONTENT_SUBMENU_PAGES_LINK_LOCATOR['locator'])
        self.blocks = Blocks(CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR['strategy'],
                             CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR['locator'])
        self.widgets = Widgets(CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR['strategy'],
                               CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR['locator'])
        self.templates = Templates(CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR['strategy'],
                                   CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR['locator'])
        self.media_gallery = MediaGallery(CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR['strategy'],
                                          CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR['locator'])
        self.design_configuration = DesignConfiguration(
            CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR['strategy'],
            CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR['locator'])
        self.design_themes = DesignThemes(CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR['strategy'],
                                          CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR['locator'])
        self.design_schedule = DesignSchedule(CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR['strategy'],
                                              CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR['locator'])

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
