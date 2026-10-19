class LoginPage():
    def __init__(self, page):
        self.page = page
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.error_message = self.page.locator("h3[data-test='error']")

    def load(self):
        self.page.goto("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self

    def is_logged_in(self):
        return "inventory.html" in self.page.url

    def get_error_message(self):
        return self.error_message.inner_text()
