from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 3000})
    page.goto("http://localhost:8000/works/kariya-02/index.html")
    page.screenshot(path="kariya_02_screenshot.png", full_page=True)
    browser.close()
