from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser_name):
    if browser_name.lower() == 'chrome':
        return webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name.lower() == 'firefox':
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')
