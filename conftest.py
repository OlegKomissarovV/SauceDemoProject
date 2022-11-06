import pytest
from selenium import webdriver as WB
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser...")
    browser = WB.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print("\nquit browser...")
    browser.quit()
