import core_config.all as config
from stere.areas import Area
from stere.fields import Root
from pages.backend.fields.content_submenu_links import *

class ContentSubmenu(Area):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Root(config.ADMIN_MENU_ROOT['strategy'], config.ADMIN_MENU_ROOT['locator'])
        self.pages = Pages(config.CONTENT_SUBMENU_PAGES_LINK_LOCATOR['strategy'], config.CONTENT_SUBMENU_PAGES_LINK_LOCATOR['locator'])
        self.blocks = Blocks(config.CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR['strategy'], config.CONTENT_SUBMENU_BLOCKS_LINK_LOCATOR['locator'])
        self.widgets = Widgets(config.CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR['strategy'], config.CONTENT_SUBMENU_WIDGETS_LINK_LOCATOR['locator'])
        self.templates = Templates(config.CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR['strategy'], config.CONTENT_SUBMENU_TEMPLATES_LINK_LOCATOR['locator'])
        self.media_gallery = MediaGallery(config.CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR['strategy'], config.CONTENT_SUBMENU_MEDIA_GALLERY_LINK_LOCATOR['locator'])
        self.design_configuration = DesignConfiguration(config.CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR['strategy'], config.CONTENT_SUBMENU_DESIGN_CONFIGURATION_LINK_LOCATOR['locator'])
        self.design_themes = DesignThemes(config.CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR['strategy'], config.CONTENT_SUBMENU_DESIGN_THEMES_LINK_LOCATOR['locator'])
        self.design_schedule = DesignSchedule(config.CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR['strategy'], config.CONTENT_SUBMENU_DESIGN_SCHEDULE_LINK_LOCATOR['locator'])