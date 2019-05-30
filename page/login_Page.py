from base.base import Base
from page.elements_Login_Part import ElementsLoginPart


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def lp_click_go_login(self):
        self.click_element(ElementsLoginPart.login_go_login_xpath)

    def lp_input_username(self, text):
        self.send_element(ElementsLoginPart.login_input_username_id, text)

    def lp_input_password(self, text):
        self.send_element(ElementsLoginPart.login_input_password_id, text)

    def lp_click_login_btn(self):
        self.click_element(ElementsLoginPart.login_click_login_btn_id)

    def lp_get_no_user_btn(self):
        self.get_element(ElementsLoginPart.login_get_no_user_btn_xpath)

    def lp_click_close_login_page_btn(self):
        self.click_element(ElementsLoginPart.login_close_login_page_btn_id)

    def lp_if_login_btn(self):
        self.get_element(ElementsLoginPart.login_click_login_btn_id, timeout=10)
