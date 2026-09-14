from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_TC006_verify_product_listing_display(logged_in_driver):
    products = logged_in_driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(products) > 0


def test_TC009_verify_product_detail_display(logged_in_driver):
    product_name = logged_in_driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    product_name.click()

    detail_title = logged_in_driver.find_element(
        By.CLASS_NAME,
        "inventory_details_name"
    )

    assert detail_title.is_displayed()


def test_TC010_sort_products_by_name_ascending(logged_in_driver):
    sort_dropdown = logged_in_driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    Select(sort_dropdown).select_by_value("az")

    product_names = logged_in_driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    product_name_list = [
        product.text for product in product_names
    ]

    assert product_name_list == sorted(product_name_list)