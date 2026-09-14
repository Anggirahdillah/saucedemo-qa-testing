from selenium.webdriver.common.by import By


def test_TC007_add_product_to_cart(logged_in_driver):
    add_to_cart_button = logged_in_driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    add_to_cart_button.click()

    cart_badge = logged_in_driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert cart_badge.text == "1"


def test_TC008_remove_product_from_products_page(logged_in_driver):
    add_to_cart_button = logged_in_driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    add_to_cart_button.click()

    remove_button = logged_in_driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"
    )

    remove_button.click()

    cart_badges = logged_in_driver.find_elements(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert len(cart_badges) == 0


def test_TC020_remove_product_from_cart_page(logged_in_driver):
    add_to_cart_button = logged_in_driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    add_to_cart_button.click()

    cart_button = logged_in_driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    cart_button.click()

    remove_button = logged_in_driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"
    )

    remove_button.click()

    cart_items = logged_in_driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )

    assert len(cart_items) == 0


def test_TC021_remove_all_products_from_cart(logged_in_driver):
    products = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt"
    ]

    for product in products:
        add_button = logged_in_driver.find_element(
            By.ID,
            f"add-to-cart-{product}"
        )

        add_button.click()

    cart_button = logged_in_driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    cart_button.click()

    for product in products:
        remove_button = logged_in_driver.find_element(
            By.ID,
            f"remove-{product}"
        )

        remove_button.click()

    cart_items = logged_in_driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )

    assert len(cart_items) == 0


def test_TC027_access_empty_cart(logged_in_driver):
    cart_button = logged_in_driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    cart_button.click()

    cart_items = logged_in_driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )

    assert len(cart_items) == 0