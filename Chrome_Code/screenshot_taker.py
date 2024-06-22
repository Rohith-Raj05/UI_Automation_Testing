
import os
import time
from datetime import datetime
from web_driver import get_webdriver
import logging

logging.basicConfig(level=logging.INFO)


def take_full_page_screenshot(driver, file_path, width):
    # Get the height of the entire page
    web_page_height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
    )
    driver.set_window_size(width, web_page_height)

    # Take a full-page screenshot
    driver.save_screenshot(file_path)


def take_screenshot(url, browser, width, height, idx):
    driver = None
    try:
        driver = get_webdriver(browser)
        driver.get(url)
        logging.info(f"Loading {url} on {browser}")

        time.sleep(5)  # Wait for the page to load fully

        folder_type = "Desktop" if width >= 1366 else "Mobile"
        folder_name = f"URL{idx}_screenshots/{browser.capitalize()}/{folder_type}/{width}x{height}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        screenshot_path = os.path.join(folder_name, f"{timestamp}.png")
        take_full_page_screenshot(driver, screenshot_path, width)
        logging.info(f"Screenshot saved to {screenshot_path}")
    except Exception as e:
        logging.error(f"Error taking screenshot for {url} on {browser}: {e}")
    finally:
        if driver:
            driver.quit()
