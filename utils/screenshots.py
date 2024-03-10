import os
import time
from splinter.browser import Browser

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
parent_directory = os.path.dirname(current_directory)
screenshot_directory = os.path.join(parent_directory, "screenshots")


def take(browser: Browser, filename: str, implicit_wait: int = 0) -> None:
    time.sleep(implicit_wait)
    browser.screenshot(os.path.join(screenshot_directory, filename))


def cleanup() -> None:
    files = os.listdir(screenshot_directory)
    for file in files:
        if file == '.gitkeep':
            continue
        os.remove(os.path.join(screenshot_directory, file))
