from playwright.sync_api import Page, Locator
import config


class IndexPage:

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_text_login_button(self, page: Page) -> Locator:
        print('test case--->', page.get_by_text("Войти"))
        return page.get_by_text("Войти")