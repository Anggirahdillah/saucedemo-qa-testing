import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


# Fixture untuk membuka dan menutup browser
@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit()


# TC-001
def test_TC001_login_with_valid_credentials(driver):
    # Input username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Input password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Klik tombol Login
    driver.find_element(By.ID, "login-button").click()

    # Verifikasi berhasil masuk ke halaman Products
    assert "inventory.html" in driver.current_url

    # Verifikasi judul halaman
    page_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Products"


# TC-002
def test_TC002_login_with_wrong_password(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("wrong_password")

    driver.find_element(By.ID, "login-button").click()

    # Ambil pesan error
    error_message = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    ).text

    # Verifikasi pesan error
    assert "Username and password do not match" in error_message


# TC-003
def test_TC003_login_with_wrong_username(driver):
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    ).text

    assert "Username and password do not match" in error_message


# TC-004
def test_TC004_login_with_empty_username(driver):
    # Username sengaja tidak diisi
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    ).text

    assert "Username is required" in error_message


# TC-005
def test_TC005_login_with_empty_password(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Password sengaja tidak diisi
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    ).text

    assert "Password is required" in error_message