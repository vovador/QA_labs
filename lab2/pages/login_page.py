from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username: str, password: str):
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')
