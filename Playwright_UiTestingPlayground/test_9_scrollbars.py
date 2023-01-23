#http://uitestingplayground.com/scrollbars

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.click('text=Scrollbars')
    page.locator("#hidingButton").click()
    page.close()
    print('ok')
    