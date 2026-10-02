from playwright.sync_api import sync_playwright
from datetime import datetime
from pathlib import Path

print("Starting the Cricbuzz automation script...")
start_time = datetime.now()

# Save the output beside this Python file
output_folder = Path(__file__).resolve().parent

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(viewport={"width": 1366, "height": 900})
    page.set_default_navigation_timeout(60000)

    try:
        print("Step 1: Open Cricbuzz live scores...")
        page.goto(
            "https://www.cricbuzz.com/cricket-match/live-scores",
            wait_until="domcontentloaded"
        )

        print("Step 2: Click the match you want in the browser.")
        print("Wait until its score appears and dismiss any popup.")
        input("Then return to this terminal and press Enter...")

        page.wait_for_load_state("domcontentloaded")

        print("Step 3: Save the match screenshot...")
        screenshot_path = output_folder / "cricbuzz_live_match.png"
        page.screenshot(path=str(screenshot_path), full_page=True)

        print("Step 4: Save the visible match report...")
        report_path = output_folder / "cricbuzz_match_report.txt"
        match_text = page.locator("body").inner_text()

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"Captured at: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            f.write(f"Page title: {page.title()}\n")
            f.write(f"Match URL: {page.url}\n\n")
            f.write(match_text)

        print(f"Screenshot saved: {screenshot_path}")
        print(f"Report saved: {report_path}")

    finally:
        print("Step 5: Close the browser...")
        browser.close()

print(f"Script completed in: {datetime.now() - start_time}")