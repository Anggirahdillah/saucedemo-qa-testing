from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def wait_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def click_element(driver, locator):
    wait_clickable(driver, locator).click()


def add_backpack(driver):
    click_element(
        driver,
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )


def add_bike_light(driver):
    click_element(
        driver,
        (By.ID, "add-to-cart-sauce-labs-bike-light")
    )


def open_cart(driver):
    click_element(
        driver,
        (By.CLASS_NAME, "shopping_cart_link")
    )


def open_checkout(driver):
    click_element(
        driver,
        (By.ID, "checkout")
    )


def fill_checkout_information(
    driver,
    first_name="Anggi",
    last_name="Rahdillah",
    postal_code="12345"
):
    wait_visible(
        driver,
        (By.ID, "first-name")
    ).send_keys(first_name)

    wait_visible(
        driver,
        (By.ID, "last-name")
    ).send_keys(last_name)

    wait_visible(
        driver,
        (By.ID, "postal-code")
    ).send_keys(postal_code)


def click_continue(driver):
    click_element(
        driver,
        (By.ID, "continue")
    )


def get_error_message(driver):
    return wait_visible(
        driver,
        (By.CSS_SELECTOR, "[data-test='error']")
    ).text


# =========================================================
# TC013 - CHECKOUT DENGAN INFORMASI VALID
# =========================================================

def test_TC013_checkout_with_valid_information(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)
    open_cart(driver)
    open_checkout(driver)

    fill_checkout_information(driver)

    click_continue(driver)

    title = wait_visible(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert title.text == "Checkout: Overview"

    click_element(
        driver,
        (By.ID, "finish")
    )

    complete_message = wait_visible(
        driver,
        (By.CLASS_NAME, "complete-header")
    )

    assert complete_message.text == "Thank you for your order!"

# =========================================================
# TC014 - CHECKOUT DENGAN INFORMASI TIDAK LENGKAP
# =========================================================

def test_TC014_checkout_with_incomplete_information(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)
    open_cart(driver)
    open_checkout(driver)

    click_continue(driver)

    error_message = get_error_message(driver)

    assert error_message == "Error: First Name is required"


# =========================================================
# TC015 - LAST NAME KOSONG
# =========================================================

def test_TC015_checkout_with_empty_last_name(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)
    open_cart(driver)
    open_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="Anggi",
        last_name="",
        postal_code="12345"
    )

    click_continue(driver)

    error_message = get_error_message(driver)

    assert error_message == "Error: Last Name is required"


# =========================================================
# TC016 - POSTAL CODE KOSONG
# =========================================================

def test_TC016_checkout_with_empty_postal_code(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)
    open_cart(driver)
    open_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="Anggi",
        last_name="Rahdillah",
        postal_code=""
    )

    click_continue(driver)

    error_message = get_error_message(driver)

    assert error_message == "Error: Postal Code is required"


# =========================================================
# TC017 - FIRST NAME KOSONG
# =========================================================

def test_TC017_checkout_with_empty_first_name(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)
    open_cart(driver)
    open_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="",
        last_name="Rahdillah",
        postal_code="12345"
    )

    click_continue(driver)

    error_message = get_error_message(driver)

    assert error_message == "Error: First Name is required"


# =========================================================
# TC018 - POSTAL CODE TIDAK VALID
# =========================================================
def test_TC018_checkout_with_invalid_postal_code(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)
    open_cart(driver)
    open_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="Anggi",
        last_name="Rahdillah",
        postal_code="abc123"
    )

    click_continue(driver)

    # Sistem seharusnya menampilkan pesan validasi
    error_message = get_error_message(driver)

    assert error_message is not None

    # Sistem seharusnya tidak melanjutkan ke Checkout: Overview
    assert "/checkout-step-two.html" not in driver.current_url


# =========================================================
# TC019 - CHECKOUT DENGAN MULTIPLE PRODUCTS
# =========================================================

def test_TC019_checkout_with_multiple_products(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)
    add_bike_light(driver)

    open_cart(driver)

    cart_badge = wait_visible(
        driver,
        (By.CLASS_NAME, "shopping_cart_badge")
    )

    assert cart_badge.text == "2"

    open_checkout(driver)

    fill_checkout_information(driver)

    click_continue(driver)

    title = wait_visible(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert title.text == "Checkout: Overview"

    checkout_items = driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )

    assert len(checkout_items) == 2


# =========================================================
# TC022 - VERIFIKASI TOTAL HARGA CHECKOUT
# =========================================================

def test_TC022_verify_checkout_total_price(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)
    add_bike_light(driver)

    open_cart(driver)
    open_checkout(driver)

    fill_checkout_information(driver)

    click_continue(driver)

    title = wait_visible(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert title.text == "Checkout: Overview"

    # Mengambil seluruh harga produk pada halaman overview
    price_elements = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_price"
    )

    expected_subtotal = 0

    for element in price_elements:
        price = float(
            element.text.replace("$", "").strip()
        )
        expected_subtotal += price

    # Mengambil subtotal yang ditampilkan aplikasi
    subtotal_element = wait_visible(
        driver,
        (By.CLASS_NAME, "summary_subtotal_label")
    )

    displayed_subtotal = float(
        subtotal_element.text.split("$")[1]
    )

    assert displayed_subtotal == expected_subtotal

    # Mengambil pajak
    tax_element = wait_visible(
        driver,
        (By.CLASS_NAME, "summary_tax_label")
    )

    displayed_tax = float(
        tax_element.text.split("$")[1]
    )

    # Mengambil total akhir
    total_element = wait_visible(
        driver,
        (By.CLASS_NAME, "summary_total_label")
    )

    displayed_total = float(
        total_element.text.split("$")[1]
    )

    expected_total = displayed_subtotal + displayed_tax

    assert displayed_total == expected_total


# =========================================================
# TC023 - CANCEL CHECKOUT DARI HALAMAN INFORMASI
# =========================================================

def test_TC023_cancel_checkout_from_information_page(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)

    open_cart(driver)
    open_checkout(driver)

    title = wait_visible(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert title.text == "Checkout: Your Information"

    click_element(
        driver,
        (By.ID, "cancel")
    )

    # Setelah cancel, kembali ke halaman Your Cart
    cart_title = wait_visible(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert cart_title.text == "Your Cart"
# =========================================================
# TC024 - CANCEL CHECKOUT DARI HALAMAN OVERVIEW
# =========================================================

def test_TC024_cancel_checkout_from_overview_page(logged_in_driver):
    driver = logged_in_driver

    add_backpack(driver)

    open_cart(driver)
    open_checkout(driver)

    fill_checkout_information(driver)

    click_continue(driver)

    title = wait_visible(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert title.text == "Checkout: Overview"

    click_element(
        driver,
        (By.ID, "cancel")
    )

    # Setelah cancel dari overview, kembali ke halaman Products
    products_title = wait_visible(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert products_title.text == "Products"