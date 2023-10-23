class Login:

    def __init__(self, page):
        self.page = page
        self.goto_web_page = self.page.goto("https://www.saucedemo.com/")
        self.username_input = self.page.locator("[data-test=\"username\"]")
        self.password_input = self.page.locator("[data-test=\"password\"]")
        self.login_button = self.page.locator("[data-test=\"login-button\"]")

    def login(self, username: str, password: str):
        self.goto_web_page()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
