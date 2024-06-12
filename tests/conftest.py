import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tocka_project.utils import attach

@pytest.fixture(scope="session")
def base_url():
    return "https://tochka.com/"

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    driver.page_load_strategy = "eager"

    yield driver

    attach.add_screenshot(driver)
    attach.add_logs(driver)
    attach.add_video(driver)
    attach.add_html(driver)

    driver.quit()
