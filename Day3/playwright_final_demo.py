from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the Playwright automation script...")
start_time = datetime.now()


#Daily weather report bot
#chromium --> weather site --> extract the report --> screen shot --> final text file
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Step 1: Go to the weather website...")
    page.goto("https://weather.com/", wait_until="domcontentloaded")
    page.screenshot(path="weather.png")

    print("Step 2: Extract the full data of the weather website...")
    full_data = page.content()

    print("Step 3: Save the extracted data to a text file...")
    with open("weather_report.txt", "w", encoding="utf-8") as f:
        f.write(full_data)

    print("Step 4: Take a screenshot of the weather website...")
    page.screenshot(path="weather_screenshot.png")

    print("Step 5: Close the browser...")
    browser.close()
print(f"script completed at {datetime.now() - start_time}")
