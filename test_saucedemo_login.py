from playwright.sync_api import Page, expect

def test_standard_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    # Perform login using standard user
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert that the header has text "Swag Labs" to indicate login success
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")

def test_lockedout_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Perform login using locked out user
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert error message to indicate login fail.
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
