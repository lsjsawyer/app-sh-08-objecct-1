from page.main_page import MainPage
from page.login_Page import LoginPage
from page.mine_Page import MinePage
from page.settings_Page import SettingsPage

class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_main_page(self):
        return MainPage(self.driver)

    def get_login_page(self):
        return LoginPage(self.driver)

    def get_mine_page(self):
        return MinePage(self.driver)

    def get_settings_page(self):
        return SettingsPage(self.driver)


