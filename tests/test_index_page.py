import pytest
import pages
import time

class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.get_text_login_button(page).click()
        time.sleep(10)

