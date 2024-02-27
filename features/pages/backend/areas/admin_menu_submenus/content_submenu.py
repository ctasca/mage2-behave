import features.core_config.backend.backend_locators as bl
from stere.areas import Area
from stere.fields import Root
from features.pages.backend.fields.content_submenu_links import *
from typing import List


class ContentSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(bl.ADMIN_MENU_ROOT['strategy'], bl.ADMIN_MENU_ROOT['locator'])
        self.pages = Pages(bl.CONTENT_SUBMENU_PAGES_LINK_LOCATOR['strategy'],
                           bl.CONTENT_SUBMENU_PAGES_LINK_LOCATOR['locator'])
        self.blocks = Blocks(bl.CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR['strategy'],
                             bl.CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR['locator'])
        self.widgets = Widgets(bl.CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR['strategy'],
                               bl.CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR['locator'])
        self.templates = Templates(bl.CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR['strategy'],
                                   bl.CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR['locator'])
        self.media_gallery = MediaGallery(bl.CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR['strategy'],
                                          bl.CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR['locator'])
        self.design_configuration = DesignConfiguration(
            bl.CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR['strategy'],
            bl.CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR['locator'])
        self.design_themes = DesignThemes(bl.CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR['strategy'],
                                          bl.CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR['locator'])
        self.design_schedule = DesignSchedule(bl.CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR['strategy'],
                                              bl.CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR['locator'])

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
