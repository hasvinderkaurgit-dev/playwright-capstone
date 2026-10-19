import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def inventory_page(page):
    LoginPage(page).load().login("standard_user", "secret_sauce")
    expect(page).to_have_url(InventoryPage.URL)
    return InventoryPage(page)
