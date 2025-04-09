from playwright.sync_api import sync_playwright

def upload_to_kdp(title, pdf_path, cover_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://kdp.amazon.com")
        # login and upload logic here
        browser.close()
