from playwright.sync_api import sync_playwright


class PlaywrightFactory:

    def launch_browser(self):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        return  page , browser , playwright



