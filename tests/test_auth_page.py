import pytest
import pages
import time


class TestAuthPage:

    @staticmethod
    def open_current_auth_page(page):
        pages.index_page.open_index_page(page)
        pages.auth_page.get_login_button(page).click()
        pages.auth_page.get_login_by_password_button(page).click()

    @staticmethod
    def get_h1(page):
        return page.query_selector('h1')

    @staticmethod
    def select_phone_tab(page):
        tab = page.get_by_text('Телефон').first
        tab.click()

    def test_show_all_auth_methods_tabs(self, page):
        self.open_current_auth_page(page)
        assert page.get_by_text('Телефон') is not None
        assert page.get_by_text('Почта') is not None
        assert page.get_by_text('Логин') is not None
        assert page.get_by_text('Лицевой счет') is not None

    def test_active_email_tab(self, page):
        self.open_current_auth_page(page)
        element = page.get_by_text('Почта').first
        element.click()
        assert 'rt-tab--active' in element.get_attribute("class")

    def test_active_login_tab(self, page):
        self.open_current_auth_page(page)
        element = page.get_by_text('Логин').first
        element.click()
        assert 'rt-tab--active' in element.get_attribute("class")

    def test_active_account_tab(self, page):
        self.open_current_auth_page(page)
        element = page.get_by_text('Лицевой счёт').first
        element.click()
        assert 'rt-tab--active' in element.get_attribute("class")

    def test_icorrect_password_or_captcha(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        phone_input = page.query_selector('#username')
        password_input = page.query_selector('#password')
        submit_button = page.query_selector('#kc-login')
        phone_input.fill('+77777777777')
        password_input.fill('test')
        submit_button.click()
        time.sleep(3)
        error_block = page.query_selector('.card-error')
        captcha_image = page.query_selector('.rt-captcha__image')
        if captcha_image:
            assert 'Неверно введен текст с картинки' in error_block.inner_text()
        else:
            assert 'Неверный логин или пароль' in error_block.inner_text()

    def test_show_password(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        eye_password_icon = page.query_selector('.rt-eye-icon')
        assert eye_password_icon.get_attribute('isOpen') == 'false'
        eye_password_icon.click()
        assert eye_password_icon.get_attribute('isOpen') == 'true'

    def test_remember_me_checkbox(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        checkbox_element = page.query_selector('.rt-checkbox')
        checkbox_label = page.get_by_text('Запомнить меня')
        if 'rt-checkbox--checked' in checkbox_element.get_attribute('class').split():
            checkbox_label.click()
            assert 'rt-checkbox--checked' not in checkbox_element.get_attribute('class').split()
        else:
            checkbox_label.click()
            assert 'rt-checkbox--checked' in checkbox_element.get_attribute('class').split()

    def test_forget_password(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        forgot_password_element = page.query_selector('#forgot_password')
        forgot_password_element.click()
        time.sleep(3)
        title_h1 = self.get_h1(page)
        assert title_h1.inner_text() == 'Восстановление пароля'

    def test_back_to_otp_btn(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        back_to_otp_btn_element = page.query_selector('#back_to_otp_btn')
        back_to_otp_btn_element.click()
        time.sleep(3)
        title_h1 = self.get_h1(page)
        assert title_h1.inner_text() == 'Авторизация по коду'

    def test_enter_from_vk(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        vk_icon_button = page.query_selector('#oidc_vk')
        vk_icon_button.click()
        time.sleep(3)
        assert 'id.vk.com' in page.url

    def test_enter_from_ok(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        ok_icon_button = page.query_selector('#oidc_ok')
        ok_icon_button.click()
        time.sleep(3)
        assert 'connect.ok.ru' in page.url

    def test_enter_from_mailru(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        mail_icon_button = page.query_selector('#oidc_mail')
        mail_icon_button.click()
        time.sleep(3)
        assert 'connect.mail.ru' in page.url

    def test_register(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        register_button = page.query_selector('#kc-register')
        register_button.click()
        time.sleep(3)
        title_h1 = self.get_h1(page)
        assert title_h1.inner_text() == 'Регистрация'

    def test_register_personal_data(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        register_button = page.query_selector('#kc-register')
        register_button.click()
        time.sleep(3)
        personal_data_label = page.get_by_text('Личные данные')
        name_input = page.query_selector('[name="firstName"]')
        last_name_input = page.query_selector('[name="lastName"]')
        assert personal_data_label is not None
        assert name_input is not None
        assert last_name_input is not None

    def test_register_entered_data(self, page):
        self.open_current_auth_page(page)
        self.select_phone_tab(page)
        register_button = page.query_selector('#kc-register')
        register_button.click()
        time.sleep(3)
        entered_data_label = page.get_by_text('Данные для входа')
        email_input = page.query_selector('#address')
        password_input = page.query_selector('#password')
        confirm_password_input = page.query_selector('#password-confirm')
        assert entered_data_label is not None
        assert email_input is not None
        assert password_input is not None
        assert confirm_password_input is not None
