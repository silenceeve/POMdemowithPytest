import pytest
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.login_page import LoginPage

@pytest.fixture()
def driver():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)

        yield driver

    finally:
        driver.close()
        driver.quit()

"""
@pytest.mark.parametrize("username","password",[
    ("test","test"),
    ("user1","pass1"),
    ("user2","pass2")
])
"""

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(5)
    login_page.enter_username("test")
    login_page.enter_password("test")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)


    assert "Successful" in driver.page_source
    time.sleep(1)

# heyuchen mengpocheng