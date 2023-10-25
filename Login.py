class Login:

    def __init__(self, page, playwright):
        self.page = page
        playwright.selectors.set_test_id_attribute("data-test")
        self.username_input = self.page.locator("[data-test=\"username\"]")
        self.password_input = self.page.locator("[data-test=\"password\"]")
        self.login_button = self.page.locator("[data-test=\"login-button\"]")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
