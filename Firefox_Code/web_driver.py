from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_webdriver(browser):
    if browser == 'chrome':
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Run in headless mode
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # Run in headless mode
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    else:
        raise ValueError("Unsupported browser!")
    return driver
