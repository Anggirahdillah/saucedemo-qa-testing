from selenium.webdriver.common.by import By


# TC-025
def test_TC025_reset_app_state(logged_in_driver):
    # Tambah produk ke cart
    add_to_cart_button = logged_in_driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )
    add_to_cart_button.click()

    # Pastikan produk masuk cart
    cart_badge = logged_in_driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert cart_badge.text == "1"

    # Buka sidebar
    logged_in_driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    ).click()

    # Klik Reset App State
    logged_in_driver.find_element(
        By.ID,
        "reset_sidebar_link"
    ).click()

    # Pastikan badge cart sudah hilang
    cart_badges = logged_in_driver.find_elements(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert len(cart_badges) == 0


# TC-027
def test_TC027_empty_cart(logged_in_driver):
    # Buka cart tanpa menambahkan produk
    logged_in_driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    # Cari item di cart
    cart_items = logged_in_driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )

    # Cart harus kosong
    assert len(cart_items) == 0