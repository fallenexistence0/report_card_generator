from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        channel="chromium",
        headless=True
    )
    print("Browser launched")

    page = browser.new_page()
    print("Page created")

    page.set_content("<h1>Test</h1>")
    page.pdf(path="test.pdf")

    browser.close()
    print("Success!")