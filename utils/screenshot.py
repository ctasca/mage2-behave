import os
import time
from splinter.browser import Browser

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
parent_directory = os.path.dirname(current_directory)
screenshot_directory = os.path.join(parent_directory, "screenshots")


def take(browser: Browser, filename: str, wait_time: int = 3) -> None:
    time.sleep(wait_time)
    browser.screenshot("{}/{}".format(screenshot_directory, filename))


def cleanup() -> None:
    files = os.listdir(screenshot_directory)
    for file in files:
        if file == '.gitkeep':
            continue
        os.remove(os.path.join(screenshot_directory, file))
