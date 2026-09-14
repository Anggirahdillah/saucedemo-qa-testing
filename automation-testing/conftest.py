import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()

    # Menggunakan mode Incognito agar tidak memakai profile Chrome utama
    chrome_options.add_argument("--incognito")

    # Menonaktifkan notifikasi dan password manager
    chrome_options.add_argument("--disable-notifications")

    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
    )

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    driver.find_element(
        By.ID,
        "user-name"
    ).send_keys("standard_user")

    driver.find_element(
        By.ID,
        "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID,
        "login-button"
    ).click()

    return driver