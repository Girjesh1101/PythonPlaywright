class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def fill(self, ele , value):
        self.page.locator(ele).fill(value)

    def click(self, ele):
        self.page.locator(ele).click()