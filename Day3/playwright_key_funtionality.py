from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.google.com", wait_until="domcontentloaded")
    page.screenshot(path="google.png")

    page.goto("https://weather.com/", wait_until="domcontentloaded")
    page.screenshot(path="weather.png")

    print("Page title:", page.title())

    input("Press Enter in the terminal to close the browser...")
    browser.close()
    