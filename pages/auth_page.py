from playwright.sync_api import Page, Locator

class AuthPage:
    def get_login_button(self, page: Page) -> Locator:
        return page.get_by_text("Войти")

    def get_login_by_password_button(self, page: Page) -> Locator:
        return page.get_by_text("Войти с паролем")

    def get_auth_phone_method(self, page: Page) -> Locator:
        return page.get_attribute("#t-btn-tab-phone")

