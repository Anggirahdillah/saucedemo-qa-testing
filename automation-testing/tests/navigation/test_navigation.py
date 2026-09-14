from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_TC011_sidebar_menu_display(logged_in_driver):
    wait = WebDriverWait(logged_in_driver, 10)

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "react-burger-menu-btn")
        )
    ).click()

    sidebar = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "bm-menu-wrap")
        )
    )

    assert sidebar.is_displayed()


def test_TC012_logout(logged_in_driver):
    wait = WebDriverWait(logged_in_driver, 10)

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "react-burger-menu-btn")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "logout_sidebar_link")
        )
    ).click()

    assert wait.until(
        EC.visibility_of_element_located(
            (By.ID, "login-button")
        )
    ).is_displayed()