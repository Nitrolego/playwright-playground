from playwright.sync_api import Page, expect

def test_checkout_full_flow(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Login flow as standard user
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")

    # Assert that the header has text "Swag Labs" to indicate login success
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")

    # Adding multiple items to cart
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()

    # Assert that clicking on add to cart is clicked
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"remove-sauce-labs-bike-light\"]")).to_contain_text("Remove")

    # Checkout flow
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("Athena")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").fill("Michaels")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("25686")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()

    # Asserts success of order
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")